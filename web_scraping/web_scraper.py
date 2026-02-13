from scrapy import Selector
html = '''
<html>
<body>
<div class='hello datacamp'>
<p>Hello World!</p>
<p>Enjoy DataCamp</p>
</div>
</body>
</html>
'''
sel = Selector(text= html) 
print(sel)
ps = sel.xpath('//p')
print(sel.xpath('//p').extract_first())
print(ps[1])

import requests
url = 'https://en.wikipedia.org/wiki/Web_scraping'
html = requests.get(url).content
sel = Selector(text=html)
print(sel)