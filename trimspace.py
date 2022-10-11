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

#func 47