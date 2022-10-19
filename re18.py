import re17

wordlist = re17.preprocess()
keys = sorted(wordlist.keys())
for i in range(100):
    print(keys[i],wordlist[keys[i]])
print("Keys:",len(keys))