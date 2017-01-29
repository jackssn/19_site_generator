import os
import json
import markdown
from jinja2 import Environment, FileSystemLoader


PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = 'www'
ARTICLES_HTML_PATH = os.path.join(BASE_PATH, 'articles')
ARTICLES_MD_PATH = 'articles'
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, '.')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def save_html_page(filepath, context):
    with open(filepath, 'w', encoding='utf-8') as f:
        html = render_template('templates/base.html', context)
        f.write(html)


def create_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)


def load_config_data():
    with open('config.json', encoding='utf-8') as f:
        return json.load(f)


def read_md_file(path_md):
    with open(os.path.join(ARTICLES_MD_PATH, path_md), 'r', encoding='utf-8') as f:
        return f.read()


def create_html_from_md(md_text):
    return markdown.markdown(md_text, extensions=['markdown.extensions.codehilite'])


def create_article_dict_with_link(title, text, link, topic):
    article_context = {
        'article_title': title,
        'article_text': text,
        'path': '../../../',
        'back_btn': True
    }
    return {'link': link, 'topic': topic, 'context': article_context}


if __name__ == "__main__":
    config_data = load_config_data()
    articles_dict = config_data['articles']
    topics_dict = config_data['topics']
    create_dir(BASE_PATH)
    create_dir(ARTICLES_HTML_PATH)
    for topic in topics_dict:
        create_dir(os.path.join(ARTICLES_HTML_PATH, topic['slug']))

    articles_dict_with_links = []
    for article_dict in articles_dict:
        article_title = article_dict['title']
        article_path = article_dict['source']
        article_topic = article_dict['topic']
        article_slug = '{}.html'.format(os.path.splitext(os.path.basename(article_path))[0])
        article_link = os.path.join(ARTICLES_HTML_PATH, article_topic, article_slug)
        changed_link = article_link.replace('&amp;', '&')  # it allow create correct html-linked page
        article_text = create_html_from_md(read_md_file(article_path))

        article_dict_with_link = create_article_dict_with_link(article_title, article_text, article_link, article_topic)
        articles_dict_with_links.append(article_dict_with_link)
        save_html_page(changed_link, article_dict_with_link['context'])

    index_filepath = os.path.join(BASE_PATH, "index.html")
    index_context = {
        'article_title': 'Cписок статей',
        'articles_dict_with_links': articles_dict_with_links,
        'topics_dict': topics_dict,
        'path': '../',
        'back_btn': False
    }
    save_html_page(index_filepath, index_context)
