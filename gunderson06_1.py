'''Write a program that takes a word and creates possible words that rhyme. For example, the word 
bake rhymes with cake, make, thrake, etc. Note that thrake is not an actual word, but it is a 
possible word in English. In other words, you should identify the existing onset clusters first and 
generate possible forms using the clusters. Just for your information, my program generates 56 
possible words that rhymes with bake.  '''

import re
def main():
    word = input("Word to rhyme: ")
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    start, end = stem(word)
    counter = 0
    for i in prefixes:
        counter += 1
        print(i + end)
    print('\n Number of Rhymes: ', counter)

def stem(w):
    w = str(w)
    w = w.lower()
    search = re.search('(^[^aeiou]*)([aeiouy].*)', w) # firgure out what to do with 'y'
    if search:
        start = search.group(1) 
        end = search.group(2)
        return start, end
        
if __name__ == '__main__':
    main()