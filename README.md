# Web-Scraping
This repository is intended solely for study purposes.
<br>
Author : Ayush Dongre
<br>
# Flipkart Web Scraping Project

A Python-based web scraping project to extract product details from Flipkart for various categories like phones and TVs, and compile them into structured Excel and CSV files.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

---

## Introduction

This project extracts product details such as **name, price, and specifications** (e.g., ROM, display, warranty) from Flipkart. The purpose is to analyze and organize product data for study or research purposes.

---

## Features
- Scrapes product details like **name, price, specifications** (e.g., ROM, display, warranty, etc.).
- Handles multiple product categories (e.g., phones, TVs).
- Saves the extracted data into **Excel** and **CSV** formats.
- Sorts data based on price for easier analysis.
- Gracefully handles errors like page unavailability or server issues.

---

## Prerequisites
- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`
- Flipkart account (optional, for additional access).

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/flipkart-web-scraping.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. **Run the script**:  
   Modify the base URLs for specific categories and run the script:
   ```bash
   python scrape_flipkart.py
   ```
2. **Adjust the number of pages**:  
   Update the `page_no` parameter to specify how many pages to scrape.

3. **Output files**:
   - Data is saved in `E:/FINAL/` as Excel (`.xlsx`) and CSV (`.csv`) files.
   - Example: `i_phones.xlsx`, `Combined_data_phones.csv`.

---

## Output
- **Excel/CSV Format**:
  - Columns: Product Name, Price, Specifications (e.g., ROM, Display, Camera).
  - Example:
    | Product Name      | Price | ROM       | Display     | Camera |
    |-------------------|-------|-----------|-------------|--------|
    | Samsung Galaxy S  | 9999  | 128GB ROM | 6.5" AMOLED | 64MP   |

- **Sorted Data**:  
  The data is sorted by price in ascending order.

---

## Limitations
- Flipkart's dynamic content might require adjustments to scraping logic if their website structure changes.
- Rate-limiting or CAPTCHA may interrupt scraping for larger datasets.
- Only public product data is scraped; no confidential data is accessed.

---

## Future Enhancements
- Automate CAPTCHA handling using tools like Selenium (if required).
- Add more categories, such as laptops or home appliances.
- Integrate visualization for analyzing scraped data (e.g., bar charts, histograms).
- Support for multiple export formats like JSON.

---

## Contributing
Contributions are welcome!  
Please open issues or submit pull requests for suggestions or improvements.

---


