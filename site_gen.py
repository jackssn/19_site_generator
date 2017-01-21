import os
import json
import markdown
from jinja2 import Environment, FileSystemLoader


PATH = os.path.dirname(os.path.abspath(__file__))
ARTICLES_HTML_PATH = 'www/articles'
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


def get_html_from_md(path_md):
    with open('articles/%s' % path_md, 'r', encoding='utf-8') as f:
        return markdown.markdown(f.read(), extensions=['markdown.extensions.codehilite'])


def get_article_dict_with_link(article_dict):
    article_path = article_dict['source']
    article_slug = article_path[article_path.find("/") + 1:article_path.find(".")]
    article_link = "%s/%s/%s.html" % (ARTICLES_HTML_PATH, article_dict['topic'], article_slug)
    article_context = {
        'article_title': article_dict['title'],
        'article_text': get_html_from_md(article_path),
        'path': '../../../',
        'back_btn': '<a href="javascript:history.back();" class="list-group-item">Вернуться назад</a>'
    }
    return {'link': article_link, 'context': article_context}


if __name__ == "__main__":
    config_data = load_config_data()
    articles_dict = config_data['articles']
    topics_dict = config_data['topics']
    create_dir('www')
    create_dir('www/articles')
    for topic in topics_dict:
        create_dir('%s/%s' % (ARTICLES_HTML_PATH, topic['slug']))

    articles_dict_with_links = []
    for article_dict in articles_dict:
        article_dict_with_link = get_article_dict_with_link(article_dict)
        articles_dict_with_links.append(article_dict_with_link)
        save_html_page(article_dict_with_link['link'], article_dict_with_link['context'])

    index_filepath = "www/index.html"
    index_context = {
        'article_title': 'Cписок статей',
        'articles_dict_with_links': articles_dict_with_links,
        'path': '../',
        'back_btn': ''
    }
    save_html_page(index_filepath, index_context)
