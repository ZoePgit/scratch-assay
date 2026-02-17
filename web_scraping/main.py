import sys
from playwright.sync_api import sync_playwright
def new_func(browser, titles, prices):
    for t, p in zip(titles, prices):
        print(t, "-", p)
    browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    url = 'https://www.nguyenkim.com/tim-kiem.html?tu-khoa=b%E1%BA%BFp+t%E1%BB%AB&search=&sortnk=gia-thap-den-cao&danh-muc=bep-dien'
    page.goto(url)
   
    page.wait_for_selector('.product-title a')
    titles = page.locator('.product-title a').all_inner_texts()
    prices = page.locator(".final-price").all_inner_texts()
    
    print("Product List:")
    new_func(browser, titles, prices)