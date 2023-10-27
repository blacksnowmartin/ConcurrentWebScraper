import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import threading

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

        # Save the results to a file
        with open(f"{url.replace('https://', '').replace('.', '_')}.txt", 'w') as file:
            file.write(f"URL: {url}\nTitle: {title}\nParagraph: {paragraph}\n")

        print(f"Scraped {url}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to scrape {url}: {e}")

def main():
    num_threads = 3  # Number of concurrent threads
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(scrape_url, url): url for url in urls}

    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        try:
            future.result()
        except Exception as e:
            print(f"Error scraping {url}: {e}")

if __name__ == "__main__":
    main()
    print("Scraping completed.")
