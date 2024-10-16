# Async Web Scraper

## Overview

This project is an asynchronous web scraper built using Python's `aiohttp` and `BeautifulSoup` libraries. The scraper fetches data from multiple URLs concurrently, extracts useful information, and saves the results in JSON format.

## Features

- Asynchronous fetching of web pages using `aiohttp`.
- HTML parsing with `BeautifulSoup` to extract titles, headers, and paragraphs.
- Saves scraped data in a structured JSON format.

## Requirements

- Python 3.7 or higher
- `aiohttp`
- `BeautifulSoup4`

You can install the required libraries using pip:

```bash
pip install aiohttp beautifulsoup4
