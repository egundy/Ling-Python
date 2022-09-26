nouns = 'bla dor sna'.split()
verbs = 'ha mog ge di'.split()
ivs = 'ha ge'.split()

for s in nouns:
    for v in nouns:
        if v in ivs:
            print(s,v)
        else:
            for o in nouns:
                print(s,v,o)