# 19_site_generator

## Описание

Скрипт позволяет преобразовать текст, написанный с помощью Markdown (*.md) в html-формат.

## Как использовать

Перейдите в папку с названием 19_site_generator и введите в консоль:

`python generate_site.py`

Для корректной работы скрипта необходимо установить пакеты из файла `requirements.txt`:

`pip3 install -r requirements.txt`

Также иметь json-файл для парсинга исходных страниц. Важно, чтобы папки `templates` и `static` лежали на одном уровне
с `site_gen.py`

## Результат работы

Скрипт создаст необходимые папки и файлы, преобразовав md-исходники в `html` с учетом `config.json`.
Нужные html страницы будут находиться в папке `www`:

```
www
www/index.html
www/articles/...
```

Для просмотра на локальном компьютере запустите файл `www/index.html`.
Онлайн-демонстрация доступна [по ссылке](https://jackssn.github.io/19_site_generator/www/index.html)
