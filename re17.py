import re
from lingmodules import readfile as rf

def preprocess():
    text = rf('alice.txt')
    lowtext = text.lower()
    punc = '[\.\?\-!\?\*,"\(\):\`\[\];_/~“”‘’—]'

    newtext = ''
    for c in lowtext:
        if re.search(punc,c):
            newtext += ' '
        else:
            newtext += c
    words = newtext.split()
    newwords = []
    for w in words:
        word = ''
        for c in w:
            if c != "'":
                word += c
        newwords.append(word)
    finalwords = []
    for w in newwords:
        if re.search('[0-9]',w):
            continue
        else:
            finalwords.append(w)
    wordlist = {}
    for w in finalwords:
        if len(w) > 0:
            if w in wordlist:
                wordlist[w] += 1
            else:
                wordlist[w] = 1
    return wordlist
