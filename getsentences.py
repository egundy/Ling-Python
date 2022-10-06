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