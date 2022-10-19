import re17

def readfile(filename):
    with open(filename,'r') as file_in:
        text = file_in.read()
    return text
text = readfile('alice.txt')

words = text.split()
longest_words = []
largest_len = 0
for word in words:
    if len(word) > largest_len:
        largest_len = len(word)
        longest_words = word
    elif len(word) == largest_len:
        longest_words.append(word)

print("The longest word(s) is/are:", longest_words)
print("With a lengths of:",largest_len)