import re
import sys
import readfile as rf

words = rf.readfile('alice.txt').split()
for w in words:
    m = re.search(sys.argv[1],w)
    if m:
        print(w)