words = []
lines = []
wordlengths = {}

f = open('alice.txt','r')
for line in f:
    lines.append(line)
f.close()
lines = lines[54:]

for line in lines:
    wds = line.split()
    words += wds

for wd in words:
    count = 0
    word = wd.lower()
    for l in word:
        if l in 'abcdefghijklmnopqrstuvwxyz':
            count += 1
        if count in wordlengths:
            wordlengths[count] += 1
        else:
            wordlengths[count] = 1

g = open('alice2.txt','w')

for c in wordlengths:
    clen = str(wordlengths[c])
    res = str(c) + ': ' + clen + '\n'
    g.write(res)
g.close()