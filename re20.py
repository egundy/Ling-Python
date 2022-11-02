import re
import re17

wordlist = re17.preprocess()
words = wordlist.keys()
clusters = []

for w in words:
    m = re.search('^([^aeiouy]*)[aeiouy]',w)
    if m:
        if m.end(1) == 0 and w[0] == 'y':
            onset = 'y'
        else:
            onset = w[0:m.end(1)]
        clusters.append(onset)
clusters = sorted(set(clusters))
for c in clusters:
    print("'",c,"'",sep='')
print(len(clusters))
    