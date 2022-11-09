from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import re

'''html = urlopen('https://en.wikipedia.org/wiki/Taylor_Swift')
bs(html, 'html.parser')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])'''

def fixlinks(u,l):
    res = re.sub('#.*$','',l)
    m = re.search('^http',res)
    if m:
        return res
    res = u + '/' + res
    res = re.sub('([^:]/)/+','\\1',res)
    return res

def welsh(u,t):
    welshwords = ['yn', 'y', 'i', 'a', 'o', 
                    'ei', 'ar', 'yr', 'bod', 
                    'ac', 'am', 'wedi', 'hi', 
                    'ond', 'eu', 'fel', 'na', 
                    'un', 'ni', 'mwen']
    
    n = t.lower()
    n = re.sub('[^a-z]',' ', n)
    n = re.sub(' +', ' ', n)
    wds = n.split()
    total = len(wds)
    wcount = 0
    for w in wds:
        if w in welshwords:
            wcount += 1
    percent = wcount/total
    if percent > .08:
        return True
    else:
        return False
    

def main():
    urls = [
           'http://golwg360.cymru',
           'http://www.u.arizona.edu/~hammond'
           'https://cy.wikisource.org/wiki/Hafan',
           'http://haciath.com'
           'http://techiaith.cymru',
           ]
    res = []
    already = []
    i = 1
    while urls and i < 100:
        u = urls.pop(0)
        already.append(u)
        i += 1
        try:
            w = urlopen(u, timeout=5)
            h = w.read()
            h = h.decode("UTF-8")
        except:
            print('bad url:', u)
            continue
        s = bs(h, "html.parser")
        t = s.body.get_text()
        
        if welsh(u,t):
            res.append([u,t])
            print(u,': ',len(t.split()),sep='')
            links = s.find_all('a')
            for l in links:
                lu = l.get('href')
                if lu:
                    lufixed = fixlinks(u,lu)
                    if lu not in already and lu not in urls:
                        urls.append(lufixed)
    f = open('already.txt','w')
    for u in already:
        f.write(u+'\n')
    f.close()
    f = open('urls.txt','w')
    for u in urls:
        f.write(u+"\n")
    f.close()
    f = open('results.txt','w')
    f.write('<results>\n')
    for r in res:
        f.write('<record>\n')
        u = r[0]
        t = r[1]
        f.write('<url>\n')
        f.write(u+'\n')
        f.write('<url>\n')
        f.write('<text>\n')
        f.write(t+'\n')
        f.write('<text>\n')
        f.write('<record>\n')
    f.write('<results>\n')
    f.close()
    print("Stored pages:", len(res))
        
    

if __name__ == '__main__':
    main()