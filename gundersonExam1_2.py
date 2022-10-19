'''Create a program that identifies all of the words in a string entered by the user. Begin by writing a 
function that takes a string of text as its only parameter. Your function should return a list of the words in 
the string with the punctuation marks at the edges of the words removed. The punctuation marks you 
must remove include commas, periods, question marks, hyphens, apostrophes, exclamation marks, 
colons, and semicolons. Do not remove punctuation marks that appear in the middle of a word, such as 
the apostrophes used to form a contraction. For example, if your function is provided with the string 
“Examples of contractions include: don't, isn't, and wouldn't.” then your 
function should return the list [“Examples', “of”, “contractions”, “include”, 
“don't”, “isn't”, “and”, “wouldn't”]. '''
import re

user_input = input("Enter a string that you want punctuation removed from:\n")
clean_input = re.sub(r'[^\w\d\s\']+', ' ', user_input)

print("Your cleaned list is:", clean_input.split())