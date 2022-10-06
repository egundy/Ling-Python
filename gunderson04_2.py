import re
import operator
from sys import argv

with open(argv[1],'r',encoding='utf-8') as file_in:
    text_file = file_in.read()
    
clean_text = re.sub(r'[^\w\s\_]','', text_file)
clean_text_new = re.sub(r'\_','', clean_text)
word_list = clean_text_new.lower().split()

word_freq = {}
sorted_word_dict = {}
words = []
count = 0
for word in word_list:
    words.append(word)
    if word in words:
        count += 1
        word_freq[word] = word_freq.setdefault(word, 0) + 1
sorted_word_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


sorted_dict = dict(sorted_word_freq)
with open(argv[2],'w') as file_out:
    for key, value in sorted_dict.items():
        file_out.write('%s:%s\n' % (key, value))