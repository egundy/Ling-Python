# create variables
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxz'
# ask for input for 'letter' variable
letter = input('Enter a letter of the alphabet\t')
# in case the string passed is upper case, use the .lower() function and reassign 'letter'
letter = letter.lower()

# conditional logic for if it is a vowe, consonant, y, or something else
if letter in vowels:
    print('This letter is a vowel')
elif letter in consonants:
    print('This letter is a consonant')
elif letter == 'y':
    print('Y is sometimes a vowel and sometimes a consonant')
else:
    print('The input is not a letter')