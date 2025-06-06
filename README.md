# Tech Trend Analyzer

**Утилита на Python для анализа трендов упоминаний технологий в новостных RSS-лентах.**

## Название репозитория

`tech-trend-analyzer`

## Описание

Инструмент на Python для парсинга RSS-лент ведущих IT-изданий, подсчёта упоминаний заданных технологий и агрегирования трендов во времени.

## Обзор проекта

Проект собирает заголовки и описания новостей из нескольких RSS-лент (TechCrunch, The Verge, Wired и др.), выполняет токенизацию текста, подсчитывает частоту упоминаний ключевых слов (AI, Blockchain, Python и др.) и строит временные ряды. Результаты сохраняются в CSV-файлы для последующего анализа и визуализации.

## Функции

* Загрузка и парсинг XML из нескольких RSS-лент (TechCrunch, The Verge, Wired и др.)
* Токенизация текста с помощью регулярных выражений
* Подсчёт упоминаний ключевых технологий в заголовках и описаниях
* Агрегация количества упоминаний по дате и технологии
* Экспорт сырых данных (`raw_mentions.csv`) и агрегированных трендов (`technology_trends.csv`)

## Установка

```bash
git clone https://github.com/yourusername/tech-trend-analyzer.git
cd tech-trend-analyzer
pip install -r requirements.txt
```

## Использование

1. Откройте файл `trend_analyzer.py` и настройте:

   * `FEED_URLS` — список URL RSS-лент
   * `TECH_KEYWORDS` — список технологий для отслеживания
2. Запустите скрипт:

   ```bash
   python trend_analyzer.py
   ```
3. Результаты появятся в корне проекта:

   * `raw_mentions.csv` — все отдельные упоминания
   * `technology_trends.csv` — агрегированные данные по датам и технологиям

## Лицензия

Проект распространяется под лицензией MIT. Вы можете форкать и адаптировать его для собственных нужд.
