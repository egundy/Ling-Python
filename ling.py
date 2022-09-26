import sys

vowels = 'aeiou'
word = sys.argv[1]
counter = 0
vowelcount = 0
while counter < len(word):
    if word[counter] in vowels:
        vowelcount += 1
    counter += 1
print('There are', vowelcount, 'vowels in this word')