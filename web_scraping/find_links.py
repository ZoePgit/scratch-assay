import requests
from bs4 import BeautifulSoup as Soup
import os
import csv

# Constants for the attributes to be extracted from the sitemap.
ATTRS = [".product-title a", ".final-price", ".tag-image"]

def parse_sitemap(url, csv_filename="urls.csv"):
    """Parse the sitemap at the given URL and append the data to a CSV file."""
    # Return False if the URL is not provided.
    if not url:
        return False

    # Attempt to get the content from the URL.
    response = requests.get(url)
    # Return False if the response status code is not 200 (OK).
    if response.status_code != 200:
        return False

    # Parse the XML content of the response.
    soup = Soup(response.content, "xml")

    # Recursively parse nested sitemaps.
    for sitemap in soup.find_all("sitemap"):
        product_title = sitemap.find("product-title").text
        parse_sitemap(product_title, csv_filename)

    # Define the root directory for saving the CSV file.
    root = os.path.dirname(os.path.abspath(__file__))

    # Find all URL entries in the sitemap.
    urls = soup.find_all("url")

    rows = []
    for url in urls:
        row = []
        for attr in ATTRS:
            found_attr = url.find(attr)
            # Use "n/a" if the attribute is not found, otherwise get its text.
            row.append(found_attr.text if found_attr else "n/a")
        rows.append(row)

    # Check if the file already exists
    file_exists = os.path.isfile(os.path.join(root, csv_filename))

    # Append the data to the CSV file.
    with open(os.path.join(root, csv_filename), "a+", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write the header only if the file doesn't exist
        if not file_exists:
            writer.writerow(ATTRS)
        writer.writerows(rows)

parse_sitemap("https://www.nguyenkim.com/tim-kiem.html?tu-khoa=b%E1%BA%BFp+t%E1%BB%AB&search=&sortnk=gia-thap-den-cao&danh-muc=bep-dien")

    