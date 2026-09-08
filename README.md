# Books Web Scraper

A Python web scraper that grabs book data from books.toscrape.com. It's got solid error handling and logs everything so you know what happened.

## What You Get
- Scrapes 1,000+ books across 50 pages
- Pulls 3 key fields: name, price, availability
- Saves everything to CSV (ready for Excel)
- Logs every step with timestamps so you can debug easily

## What It Does
- Automatically loops through all 50 pages
- Extracts book names, prices, and stock status
- Handles missing data gracefully (doesn't crash)
- Catches connection problems and logs them
- Exports clean, ready-to-use CSV files

## Tech Stack
- **Python 3**
- **Requests** - fetches web pages
- **BeautifulSoup 4** - parses HTML and grabs data
- **CSV** - stores the data
- **Logging** - tracks errors with timestamps

## Setup & Run

Install dependencies:
```bash
pip install requests beautifulsoup4
```

Run it:
```bash
python booktoscrap.py
```

That's it. It'll:
1. Hit all 50 pages
2. Pull book info (name, price, availability)
3. Save to `books.csv`
4. Log everything to `scraper.log`

## What You Get (Files)

**books.csv** — Your data, 1,000+ rows:
| name | price | availability |
|---|---|---|
| A Light in the Attic | £51.77 | In stock |
| Tipping the Velvet | £53.74 | In stock |
| Soumission | £50.10 | In stock |

**scraper.log** — Your activity log:
