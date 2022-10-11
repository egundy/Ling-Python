#func 43
def getsentences(t):
    splitters = '.?!'
    ss = []
    i = 0
    while i < len(t):
        s = ''
        while i < len(t) and \
            t[i] not in splitters:
                s += t[i]
                i += 1
        if i < len(t):
            s += t[i]
        i += 1
        ss.append(s)
    return ss

#func 45
def makespaces(t):
    breaks = '\n\t'
    r1 = ''
    i = 0
    while i < len(t):
        if t[i] in breaks:
            r1 += ' '
        else:
            r1 += t[i]
        i += 1
    r2 = r1[0]
    i = 1
    while i < len(r1):
        if r1 == ' ' and r2[len(r2)-1] == " ":
            i += 1
            continue
        else:
            r2 += r1[i]
        i += 1
    return r2

#func 42
def readfile(filename):
    with open(filename,'r') as file_in:
        text = file_in.read()
    return text

#func 47
def trimspaces(t):
    r1 = []
    for s in t:
        if s[0] == ' ':
            s = s[1:]
        slast = len(s) - 1
        if len(s) > 0 and s[slast == ' ']:
            s = s[:slast]
        r1.append(s)
    r2 = []
    for s in r1:
        if len(s) > 0:
            r2.append(s)
    return r2