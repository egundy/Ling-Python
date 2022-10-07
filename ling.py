import getsentences as gs
import readfile as rf
import makespaces as ms


txt = rf.readfile('alice.txt')
txt = txt[1434:]


cleanedtext = ms.makespaces(txt)
s = gs.getsentences(cleanedtext)


for i in range(10):
    print('\n',i,':',s[i],sep='')