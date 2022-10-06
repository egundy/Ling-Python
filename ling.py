import getsentences as gs
import readfile as rf

txt = rf.readfile('alice.txt')
txt = txt[1434:]
s = gs.getsentences(txt)
for i in range(10):
    print(i,s[i])