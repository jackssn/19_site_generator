# 19_site_generator

## Описание

Скрипт позволяет преобразовать текст, написанный с помощью Markdown (*.md) в html-формат.

## Как использовать

Введите в консоль:

1. `pip3 install -r requirements.txt`
2. `python site_gen.py`

Для корректной работы скрипта необходимо установить пакеты из файла `requirements.txt`, а также иметь файл в формате
`json` для парсинга исходных страниц. Важно, чтобы папки `templates` и `static` лежали на одном уровне с `site_gen.py`

## Результат работы

Скрипт создаст необходимые папки и файлы, преобразовав md-исходники в `html` с учетом `config.json`.
Нужные html страницы будут находиться в папке `www`

```
www
www/index.html
www/articles/...
```

Для просмотра запустите файл `index.html`