import bs4
import urllib.request

link = "http://www.u.arizona.edu/~hammond/"

f = urllib.request.urlopen(link)
myfile = f.write('hammond.html')
print(myfile.decode('UTF-8'))