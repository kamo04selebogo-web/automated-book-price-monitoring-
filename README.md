# Automated Book Price Monitoring System

## Overview

The Automated Book Price Monitoring System is a Python-based solution designed to streamline competitor book price monitoring for BookMarket Insights.

The system automatically collects book titles and prices across multiple product pages, validates the collected information, prevents duplicate records, records collection timestamps, and exports the results into a structured dataset.

This reduces repetitive manual data collection and provides a consistent foundation for pricing analysis and decision-making.

## Business Objective

The solution was developed to address the following requirements:

* Automate competitor book price collection
* Collect data across multiple pages
* Maintain clean and consistent records
* Prevent duplicate products
* Capture the date and time of collection
* Handle temporary connection failures
* Maintain an activity log
* Produce a structured dataset for analysis

## Solution

The system uses Python to request and process webpage content, extract relevant product information, validate the results, and store the collected data.

The workflow is:

```text
Website
   ↓
HTTP Request
   ↓
HTML Processing
   ↓
Book & Price Extraction
   ↓
Validation
   ↓
Duplicate Detection
   ↓
Timestamping
   ↓
CSV Export
   ↓
Activity Logging
```

## Key Features

### Automated Data Collection

Automatically collects book titles and prices without requiring manual entry.

### Multi-Page Processing

Follows the website's pagination to collect products across multiple pages.

### Data Validation

Checks that required information is available before a record is saved.

### Duplicate Detection

Prevents duplicate books from being added to the final dataset.

### Retry Handling

If a temporary request failure occurs, the system waits and retries the request.

### Timeout Protection

Requests use a timeout to prevent the process from waiting indefinitely.

### Timestamp Tracking

Each collected record includes the date and time at which the information was obtained.

### Activity Logging

The system records important events and errors in `scraper.log`, providing visibility into the scraping process.

### Structured Export

Collected information is exported to `books.csv` for further analysis and reporting.

## Deliverables

| File             | Purpose                             |
| ---------------- | ----------------------------------- |
| `web_scraper.py` | Main automated scraping application |
| `books.csv`      | Collected book and pricing data     |
| `scraper.log`    | Scraping activity and error log     |
| `README.md`      | Project documentation               |

## Data Structure

The generated dataset contains:

| Field          | Description                                 |
| -------------- | ------------------------------------------- |
| **Title**      | Name of the book                            |
| **Price**      | Listed book price                           |
| **Scraped At** | Date and time the information was collected |

## Technology Stack

* Python
* Requests
* BeautifulSoup
* CSV
* Logging

## Running the System

Install the required Python packages:

```bash
pip install requests beautifulsoup4
```

Run the scraper:

```bash
python web_scraper.py
```

After a successful run, the system produces:

```text
books.csv
scraper.log
```

The terminal also displays the scraping progress and a completion summary.

## Business Value

The solution provides a repeatable process for collecting competitor pricing information.

Potential applications include:

* Competitor price monitoring
* Pricing research
* Market analysis
* Product data collection
* Supporting pricing decisions
* Building historical pricing datasets

## Future Enhancements

The solution can be expanded to support:

* Scheduled automated collection
* Historical price tracking
* Price-change detection
* Automated Excel reports
* Interactive dashboards
* Email notifications
* Database storage
* Multiple competitor websites
* Configurable scraping parameters

## Data Source

The current implementation uses **Books to Scrape** as the demonstration data source.

The scraper architecture can be adapted to appropriate real-world sources while respecting their terms of use, access restrictions, and applicable rate limits.

## Project Status

**Completed**

The current version provides automated multi-page collection, validation, duplicate protection, retry handling, timestamp tracking, CSV export, and activity logging.
