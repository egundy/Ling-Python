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