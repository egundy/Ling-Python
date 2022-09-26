# define a function and pass 'word' into it
def igpay(word):
    # create a sting containing the vowels
    vowels = 'aeiou'
    # start conditional logic for pig latin translations. if the first letter is a vowel or if its a consonant
    if word[0] not in vowels: #if the first letter is a consonant
        # create a new variable called 'translated' to store the translated word
        # slice word[1:], move word[0] to the end, then add 'ay' to the word
        translated = word[1:] + word[0] + "ay"
        #print the translated word out to terminal
        print(translated)
    #conditional logic for if the first letter is a vowel
    elif word[0] in vowels:
        # create the 'translated' variable and add 'way' to the end of 'word'
        translated = word + 'way'
        # print the translated word out to terminal
        print(translated)

# call the 'igpay' functionand pass a lowered input into it
igpay(input("Enter a word you would like to translate\t").lower())