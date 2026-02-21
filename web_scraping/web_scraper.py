# Import a scrapy Selector
from scrapy import Selector
# Import requests
import requests
# Create a string html containing the html source
url = 'https://en.wikipedia.org/wiki/Web_scraping'
html = requests.get(url).content
# Create a selector object sel from html
sel = Selector(text=html)
# Print out the number of elements in the HTML document
print(len(sel.xpath('//*')))
