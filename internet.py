import bs4
import time
from urllib.request import urlopen
from multiprocessing import Pool

def mytime():
    return round(time.time() * 1000)

def geturl(url):
    start = mytime()
    data = urlopen(url, timeout=5).read()[:50]
    result = {'url' : url, 'data' : data}
    now = str(mytime() - start)
    print(url + ": " + now + "ms")
    return result

urls = ['https://en.wikipedia.org/wiki/Main_Page', 'https://google.com', 'https://news.google.com/' ]

for i in range(len(urls)):
    print(i+1, ": ", urls[i],sep='',)
print()

pool = Pool()
start = mytime()
results = pool.map(geturl,urls)
now = str(mytime() - start)
print("Total= " + now + " ms\n")