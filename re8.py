import re
import sys
from lingmodules import readfile as rf

words = set(rf('alice.txt').split())
matches = []
for w in words:
    m = re.search(sys.argv[1],w)
    if m:
        matches.append(w)

matches = set(matches)
print('there are',len(matches),'matches')