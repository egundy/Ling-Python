"""
Code for the final exam by Evan Gunderson.
This code should be able to run correctly from the terminal with user input. *Must be run in Python 3.10 or higher*
Every task will be addressed in this program and will be identified by a triple quote comment.
To use this program, type the following in the terminal: python3.1x gundersonFinal.py
"""

# global imports
import re
import nltk
import spacy

def menu(): # define the function to display the menu
    print("""
=====================================================
| 1. Capitalize a sentence correctly                |
| 2. Identify if a string is a palindrome           |
| 3. Generate a freq. list of words in a PDF        |
| 4. Pride and Prejudice similies                   |
| 5. People form Linguistics Wikipedia page         |
| 6. Use spaCy to find 78th sentence of wiki page   |
| 7. Generate tree diagram of a sentence            |
| 8. Chunk all NPs, PPs, and VPs from a sentence    |
|                                                   |
| *Type 'q' to quit*                                |
=====================================================
""")


""" Task 1: Capitalize a sentence correctly"""
def capitalize(string): # function to capitalize the appropriate characters in a string
    string = string[0].upper() + string[1:]    # capitalize the first character in the string
    string = re.sub(r'([.!?]) ([a-z])', lambda x: x.group(1) + ' ' + x.group(2).upper(), string)    # Capitalize the first non-space character after a '.', '!' or '?'
    flag = True    # While loop flag
    while flag == True:    # While loop to capitalize the 'i' if it is both preceded and followed by a space
        search_for_i = re.search(r' ([i]) ', string)   # Search for the 'i' in the string
        if search_for_i:    # If the 'i' is found, capitalize it
            string = re.sub(r' ([i]) ', lambda x: ' ' + x.group(1).upper() + ' ', string)   # Capitalize the 'i' if it is both preceded and followed by a space
        else:   # If the 'i' is not found, set the flag to False
            flag = False    # Set the flag to False to exit the while loop
    return string    # Return the string

# execute the function with user input
def ui_capitalize():
    print("""
================================================================================================          
*** Welcome to the Capitalize a sentence correctly task! ***
Is this the corect task? Type 'y' for yes or 'n' for no and return to the menu.
""")
    correct_task = input("Enter your selection: ")
    if correct_task == 'y':
        print("Thank you! Now starting the task...")
        # Get a string from the user
        string = input("Enter a string to capitalize: ")
        # Capitalize the string
        string = capitalize(string)
        # Display the string
        print(f"The correct capitalization of your sentence:\n{string}")
        print("\nThank you for using this program! Would you like to try another sentence? \n\
              Type 'y' for yes or 'n' for no and return to the menu.")
        user_input = input("Enter your selection: ")
        match user_input:
            case 'y':
                print("Thank you! Returning to the task...\n")
                ui_capitalize()
            case 'n':
                print("Thank you! Returning to the main menu...\n")  
            case _:
                # If the user does not enter a 'y' or an 'n', display an error message
                raise ValueError("You must enter a 'y' or an 'n'!")        
    elif correct_task == 'n':
        print("Thank you! Returning to the main menu...\n")
    else:
        print("You must enter a 'y' or an 'n'!")
        ui_capitalize()

""" Task 2: Identify if a string is a palindrome """
def is_palindrom(string): # function to identify if a string is a palindrome
    string = string.lower()    # Convert the string to lower case
    string = re.sub(r'[^a-z]', '', string)    # Remove all non-alphabetical characters
    if string == string[::-1]:    # If the string is equal to the reverse of the string, it is a palindrome
        return True    # Return True
    else:    # If the string is not equal to the reverse of the string, it is not a palindrome
        return False    # Return False

    
    
""" Main program loop """
def main():
    mainflag = True
    while mainflag == True:
        menu()
        print("Enter a number to select a task or 'q' to quit.")
        selection = input("Enter your selection: ")
        match selection:
            case '1':
                ui_capitalize()

            case 'q':
                print("Thank you for using this program! Goodbye!")
                mainflag = False
    
    
# Call the main function
if __name__ == '__main__':
    main()