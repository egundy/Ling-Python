from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

html = urlopen('https://en.wikipedia.org/wiki/Taylor_Swift')
soup = bs(html, 'html.parser')
wiki_links = {}

for link in soup.find_all("a"):
    url = link.get('href', "")
    if "/wiki/" in url:
        wiki_links[link.text.strip()] = url
print(wiki_links)