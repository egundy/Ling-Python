import lingmodules as lm

txt = lm.readfile('alice.txt')
txt = txt[1434:]

cleanedtext = lm.makespaces(txt)
ss = lm.getsentences(cleanedtext)
ts = lm.trimspaces(ss)

counts = {}

for s in ts:
    slength = len(s.split())
    
    if slength in counts:
        counts[slength] += 1
    else:
        counts[slength] = 1
for c in sorted(counts):
    print(c,counts[c])