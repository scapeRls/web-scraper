import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
import os

class AsyncWebScraper:
    def __init__(self, urls):
        self.urls = urls
        self.results = []

    async def fetch(self, session, url):
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Failed to fetch {url}: {response.status}")
                return None

    async def parse(self, html, url):
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else 'No Title'
        data = {
            'url': url,
            'title': title,
            'headers': [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])],
            'paragraphs': [p.get_text() for p in soup.find_all('p')]
        }
        self.results.append(data)

    async def scrape(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.urls:
                html = await self.fetch(session, url)
                if html:
                    tasks.append(self.parse(html, url))
            await asyncio.gather(*tasks)

    def save_to_json(self, filename='results.json'):
        with open(filename, 'w') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
        print(f"Results saved to {filename}")

if __name__ == "__main__":
    # List of URLs to scrape
    urls_to_scrape = [
        'https://example.com',
        'https://example.org',
        'https://example.net'
    ]
    
    scraper = AsyncWebScraper(urls_to_scrape)
    asyncio.run(scraper.scrape())
    scraper.save_to_json()
