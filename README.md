# YallaKora Web Scraper

## Project Overview
This Python-based web scraper is designed to extract football match data from the YallaKora website. By providing a specific date, users can generate a CSV file containing detailed match information, including:

- **League Type**
- **Team Names**
- **Match Results**
- **Timings**

The project utilizes the `requests` library for fetching web pages, `BeautifulSoup` for HTML parsing, and `csv` for outputting data.

## Features
- User inputs a date to scrape match data.
- Extracts data for all matches on the specified date.
- Generates a CSV file (`test.csv`) with the following columns:
  - نوع البطوله (League Type)
  - الفريق اﻻول (Team A)
  - الفريق الثانى (Team B)
  - ميعاد المباراه (Match Timing)
  - النتيجه (Resu ```

## Usage
1. Run the script:
   ```bash
   python scraper.py
   ```
2. Enter the date in `MM/DD/YY` format when prompted:
   ```
   please enter the date in MM/DD/YY: 01/01/25
   ```
3. The script will fetch match data for the specified date and save it to `test.csv`.

## CSV Output
The generated CSV file contains structured match data. Below is an example:

| نوع البطوله      | الفريق اﻻول      | الفريق الثانى      | ميعاد المباراه  | النتيجه    |
|-------------------|------------------|--------------------|-----------------|------------|
| الدوري المصري    | الأهلي           | الزمالك           | 7:00 PM        | 2 - 1      |
| الدوري الإسباني  | برشلونة         | ريال مدريد         | 10:00 PM       | 1 - 3      |

## Code Overview
The script performs the following steps:
1. Fetches the YallaKora webpage for the given date using `requests`.
2. Parses the HTML content using `BeautifulSoup`.
3. Extracts match details for all championships listed on the page.
4. Outputs the data into a structured CSV file.

### Functions
#### `main(page)`
- Entry point of the script.
- Handles data extraction and CSV generation.

#### `get_match_info(championships)`
- Extracts match details for a specific championship.
- Appends the data to a global list `matches_list`.

## Limitations
- The script assumes the website structure remains unchanged. If YallaKora updates its HTML, the scraper may require adjustments.
- Date format must strictly follow `MM/DD/YY`.


