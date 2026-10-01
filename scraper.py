import requests
import csv
import logging
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Website to scrape
url = "https://books.toscrape.com/"

# Set up logging
logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Scraper started")

# Create the CSV file
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # CSV headings
    writer.writerow(["Title", "Price", "Scraped At"])

    total_books = 0
    seen_titles = set()

    while url:

        print(f"Scraping: {url}")
        logging.info(f"Scraping page: {url}")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

        except requests.RequestException as e:
            print(f"Failed to scrape {url}: {e}")
            logging.error(f"Failed to scrape {url}: {e}")

            print("Waiting 5 seconds before retrying...")
            time.sleep(5)
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        books_on_page = soup.select("article.product_pod")

        logging.info(f"Found {len(books_on_page)} books on page")

        for book in books_on_page:

            title = book.h3.a.get("title")
            price_element = book.select_one(".price_color")

            # Check that the required information exists
            if not title or not price_element:
                logging.warning("Book with missing information skipped")
                continue

            price = price_element.text.strip()

            # Prevent duplicate books
            if title in seen_titles:
                logging.warning(f"Duplicate book skipped: {title}")
                continue

            seen_titles.add(title)

            scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([
                title,
                price,
                scraped_at
            ])

            total_books += 1

        # Find the next page
        next_button = soup.select_one("li.next a")

        if next_button:
            next_page = next_button["href"]
            url = url.rsplit("/", 1)[0] + "/" + next_page
        else:
            url = None

logging.info(f"Scraper finished. Total books collected: {total_books}")

print()
print("Scraping complete!")
print(f"Total unique books collected: {total_books}")
print("Data saved to books.csv")
print("Activity saved to scraper.log")