import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'
# ping a website or portal for information
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')
# Python library that is used for web scraping purposes to pull the data out of HTML and XML files
text = soup.find_all(text=True)
# table = soup.findAll(['p','h2','h3','h4','h5','h6'])

# print(text)
output = ''
extractlist = [
    'p',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6'
    # there may be more elements you want
]

for t in text:
    if t.parent.name in extractlist:
        output += '{} '.format(t)
# print(output)


import re
output= re.sub("\n"," ",output)
print(output)
