# Web Scraping Project

A Python web scraper that extracts book data from websites using BeautifulSoup and Requests.

## Features
- Scrapes multiple pages automatically
- Extracts structured data: Book name, Price, Availability
- Exports clean data to CSV format (Excel-ready)
- Fast and efficient scraping

## Technologies Used
- **Python 3**
- **Requests** - HTTP library for fetching web pages
- **BeautifulSoup 4** - HTML parsing and data extraction
- **CSV** - Data storage format

## Installation

```bash
pip install requests beautifulsoup4
```

## Usage

```bash
python scraper.py
```

This will:
1. Scrape all 50 pages from books.toscrape.com
2. Extract: book names, prices, and availability status
3. Save all data to `books.csv`

## Output Example

| name | price | availability |
|---|---|---|
| A Light in the Attic | £51.77 | In stock |
| Tipping the Velvet | £53.74 | In stock |
| Soumission | £50.10 | In stock |

## Project Stats
- **Total Books Scraped:** 1,000+
- **Pages Covered:** 50
- **Data Fields:** 3 (name, price, availability)
- **Output Format:** CSV

## How It Works
1. Fetches each page using `requests.get()`
2. Parses HTML structure with BeautifulSoup
3. Extracts specific data using CSS selectors
4. Writes clean data to CSV file with proper formatting

## Skills Demonstrated
- Web scraping
- Data extraction
- HTML parsing
- Python automation
- Data cleaning & structuring
