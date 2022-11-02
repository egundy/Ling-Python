import re
import sys

def consonant(s,i):
    letter = s[i]
    if letter in "aeiou":
        return False
    elif letter == 'y' and i == 0:
        return True
    elif letter == 'y' and consonant(s,i-1):
        return False
    else:
        True

def cv(w):
    res = ''
    for i in range(len(w)):
        if consonant(w,i):
            res += "C"
        else:
            res += "V"
    return res

def measure(w):
    cvword = cv(w)
    vcs = re.findall("VC", cvword)
    return len(vcs)

def rule(c,e,r,w):
    m = re.search('^(.*)'+e+'$',w)
    if m:
        s = m.group(1)
        if c(s):
            return s+r
    return None

def m1cond(x):
    if measure(x) > 0:
        return True
    return False

def edrule(w):
    x = rule(m1cond, 'ed', "", w)
    return x

def stem(w):
    res = edrule(w)
    if res:
        return res
    return w

word = 'tested'
print(stem(word))