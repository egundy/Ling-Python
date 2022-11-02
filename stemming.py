import sys
import re

def stem(w):
    m = re.search('(^.*)ed$',w)
    if m:
        return m.group(1)
    else:
        return w

word = sys.argv[1]
root = stem(word)
print(word,':\t',root, sep='')