import re,sys
from manip12 import *
def m1cond(x):
    if measure(x) > 0:
        return True
    return False

def nullcond(x):
    return True

def vcond(x):
    cvform = cv(x)
    if re.search('V', cvform):
        return True
    return False

def step1a(w):
    a = rule(nullcond, 'sses','ss',w)
    if a: return a
    b = rule(nullcond,'ies','i',w)
    if b: return b 
    c = rule(nullcond, 'ss', 'ss', w)
    if c: return c
    d = rule(nullcond, 's', '', w)
    if d: return d
    return w

def special(w):
    a = rule(nullcond, 'at','ate',w)
    if a: return a
    b = rule(nullcond,'bl','ble',w)
    if b: return b
    c = rule(nullcond, 'iz', 'ize', w)
    if c: return c
    d = specialrule(w)
    if d: return d
    e = rule(m1ocond,'','e',w)
    if e: return e
    return w

def specialrule(w):
    cvform = cv(w)
    m = re.search('CC$',cvform)
    if m:
        m2 = re.search('^(.*)([^szl])\\2',w)
        if m2:
            return m2.group(1)+m2.group(2)
    return None

def m1ocond(w):
    cvform = cv(w)
    if measure(cvform) == 1:
        m = re.search('CVC$', cvform)
        if m:
            m2 = re.search('[^xyw]$',w)
            if m2:
                return True
        return False
def m2cond(x):
    if measure(x) > 1:
        return True
    return False

def step1b(w):
    a = rule(m1cond, 'eed', 'ee', w)
    if a: return a
    b = rule(vcond, 'ed', '', w)
    if b: return special(b) 
    c = rule(vcond, 'ing', '', w)
    if c: return special(c)
    return w

def step1c(w):
    return w

def step2(w):
    return w

def step3(w):
    return w

def step4(w):
    return w

def step5a(w):
    return w

def step5b(w):
    return w

def stem(w):
    s1a = step1a(w)
    s1b = step1b(s1a)
    s1c = step1c(s1b)
    s2 = step2(s1c)
    s3 = step3(s2)
    s4 = step4(s3)
    s5a = step5a(s4)
    s5b = step5b(s5a)
    return s5b

word = sys.argv[1]
print(word)
print(stem(word))
    