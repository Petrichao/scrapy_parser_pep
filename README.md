# Асинхронный парсер информации о PEP

## 1. Описание

Проект асинхронного парсера позволяет получать список всех PEP для Python
и информацию по статусам и количеству PEP, с записью полученной информации в файлы.

---
## 2. Запуск парсера

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/Petrichao/scrapy_parser_pep.git
SSH: git clone git@github.com:Petrichao/scrapy_parser_pep.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Для запуска парсера необходимо выполнить команду:
```bash
scrapy crawl pep
```

---
## 3. Техническая информация

Скачанная информация сохраняется в папке "results/" в файлах формата .csv с указанием даты и времени парсинга.
