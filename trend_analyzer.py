import feedparser
import re
import pandas as pd
from datetime import datetime

# Configuration
FEED_URLS = [
    'https://techcrunch.com/feed/',
    'https://www.theverge.com/rss/index.xml',
    'https://www.wired.com/feed/rss',
    # Добавьте свои RSS-ленты
]
TECH_KEYWORDS = ['AI', 'Blockchain', 'Python', 'Machine Learning', 'Cloud', 'DevOps']

# Регулярное выражение для токенизации (слов)
TOKEN_PATTERN = re.compile(r"\w+", re.UNICODE)


def parse_date(entry):
    """
    Преобразует строку pubDate в объект datetime.date
    """
    # Пример: 'Wed, 29 Dec 2023 14:36:00 GMT'
    try:
        pub = entry.get('published', entry.get('updated', ''))
        dt = datetime(*entry.published_parsed[:6])
        return dt.date()
    except Exception:
        return None


def extract_text(entry):
    """
    Собирает текстовые поля: title и summary/description
    """
    text = entry.get('title', '') + ' ' + entry.get('summary', entry.get('description', ''))
    return text


def count_mentions(text, keywords):
    """
    Подсчет упоминаний каждого ключевого слова в тексте
    """
    tokens = TOKEN_PATTERN.findall(text)
    tokens_lower = [t.lower() for t in tokens]
    counts = {}
    for kw in keywords:
        counts[kw] = tokens_lower.count(kw.lower())
    return counts


def main():
    records = []

    for url in FEED_URLS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            date = parse_date(entry)
            if date is None:
                continue

            text = extract_text(entry)
            mention_counts = count_mentions(text, TECH_KEYWORDS)

            for tech, cnt in mention_counts.items():
                if cnt > 0:
                    records.append({
                        'date': date,
                        'technology': tech,
                        'count': cnt,
                        'source': url,
                        'title': entry.get('title', '').strip()
                    })

    # Создаем DataFrame
    df = pd.DataFrame(records)
    if df.empty:
        print("Нет упоминаний технологий в заданных лентах за период.")
        return

    # Группируем по дате и технологии
    trend = df.groupby(['date', 'technology'])['count'].sum().reset_index()

    # Сохраняем результаты
    trend.to_csv('technology_trends.csv', index=False)
    df.to_csv('raw_mentions.csv', index=False)

    print("Анализ завершен. Файлы 'technology_trends.csv' и 'raw_mentions.csv' сохранены.")


if __name__ == '__main__':
    main()
