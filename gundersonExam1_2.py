import re

user_input = input("Enter a string that you want punctuation removed from:\n")
clean_input = re.sub(r'[^\w\d\s\']+', ' ', user_input)

print("Your cleaned list is:", clean_input.split())