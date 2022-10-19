'''Write a program that identifies the longest word(s) in a file. Your program should output an appropriate 
message that includes the length of the longest word, along with all the words of that length that occurred 
in the file. Treat any group of non-white space characters as a word, even if it includes numbers or 
punctuation marks. Report the result using the Alice text. '''
def readfile(filename):
    with open(filename,'r') as file_in:
        text = file_in.read()
    return text

def find_longest(words):
    longest_words = []
    largest_len = 0
    for word in words:
        if len(word) > largest_len:
            largest_len = len(word)
            longest_words = word
        elif len(word) == largest_len:
            longest_words.append(word)
    return longest_words, largest_len

def main():
    text = readfile('alice.txt')
    words = text.split()
    longest = find_longest(words)
    print("The longest word(s) is/are:", longest[0])
    print("With a lengths of:", longest[1])
main()