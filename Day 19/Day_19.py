# Day 19: Web Scraping with BeautifulSoup

'''
Web Scraping using Python with a library called `BeautifulSoup`.

Web scraping allows us to extract information from websites (like titles, prices, links, etc.). This is helpful when there's no official API available.

To get started, I used two libraries:
- `requests`: to fetch the web page
- `beautifulsoup4`: to parse the HTML content

Install them (if not already):
`pip install requests beautifulsoup4`
'''

import requests
from bs4 import BeautifulSoup

# Example: Scraping quotes from http://quotes.toscrape.com (a test site for scraping)
url = "http://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract
    quotes = soup.find_all('span', class_='text')

    print("Quotes from the site:\n")
    for quote in quotes:
        print(quote.text)
else:
    print("Failed to fetch the webpage.")

'''
- Web scraping can break if the website's structure changes, so it’s important to inspect the HTML properly (Right Click → Inspect Element).
- Always check a site's terms of service before scraping. Some websites do not allow it.
'''

# Found a cool mini project I can build for Day 20 (check it out now)
