import requests
from bs4 import BeautifulSoup
import concurrent.futures

# List of URLs to scrape
urls = ['https://example.com', 'https://example.org', 'https://example.net']

# Function to scrape a URL and extract information
def scrape_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad HTTP status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the page
        title = soup.title.string
        paragraph = soup.find('p').get_text()

        # Print the results
        print(f"URL: {url}\nTitle: {title}\nParagraph: {paragraph}\n")

    except requests.exceptions.RequestException as e:
        print(f"Failed to scrape {url}: {e}")

# Use a ThreadPoolExecutor to concurrently scrape the URLs
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(scrape_url, urls)

print("Scraping completed.")
