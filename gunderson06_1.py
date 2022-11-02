'''Write a program that takes a word and creates possible words that rhyme. For example, the word 
bake rhymes with cake, make, thrake, etc. Note that thrake is not an actual word, but it is a 
possible word in English. In other words, you should identify the existing onset clusters first and 
generate possible forms using the clusters. Just for your information, my program generates 56 
possible words that rhymes with bake.  '''



import re


def main():
    word = input("Word to rhyme: ")
    word = word.split()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    start, end = stem(word)
    for i in prefixes:
        print(i,end)

def stem(w):
    w = str(w)
    w = w.lower()
    vowels = ('aeiou')
    consonants = 'bcdfghjklmnpqrstvwxyz'
    pattern = (
        '([' + consonants + ']+)?'
        '([' + vowels + ']+)?'
        '(.*)'
    )
    match = re.match(pattern, w)
    if match:
        p1 = match.group(1) or ''
        p2 = match.groups(2) or ''
        p3 = match.groups(3) or ''
        return (p1,p2 + p3)
        

if __name__ == '__main__':
    main()