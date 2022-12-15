"""
Code for the final exam by Evan Gunderson.

This code should be able to run correctly from the terminal with user input. *Must be run in Python 3.10 or higher*
Every task will be addressed in this program and will be identified by a triple quote comment.
To use this program, type the following in the terminal: python3.1x gundersonFinal.py
"""

# Imports
import re 
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk.draw
from nltk import CFG
from nltk.parse import RecursiveDescentParser
from nltk.tree import *
import spacy
from spacy import displacy
import json
import PyPDF2
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Global variables
nlp = spacy.load("en_core_web_sm")   # Load the English language model

def menu(): # define the function to display the menu
    print("""
=====================================================
| 1. Capitalize a sentence correctly                |   # complete; runs
| 2. Identify if a string is a palindrome           |   # complete; runs
| 3. Generate a freq. list of words in a PDF        |   # complete; runs
| 4. Pride and Prejudice similies                   |   # complete; runs
| 5. People form Linguistics Wikipedia page         |   # complete; runs
| 6. Use spaCy to find 78th sentence of wiki page   |   # complete; runs
| 7. Generate tree diagram of a sentence            |   # complete; runs
| 8. Chunk all NPs, PPs, and VPs from a sentence    |   # complete; runs
|                                                   |
| *Type 'q' to quit*                                |
=====================================================""")

""" functions that are used in multiple tasks """
def repeat_task(task): # function to repeat a task
    print("\nThank you for using this program! Would you like to run it again? (y/n)")   # Ask the user if they would like to run the task again
    again = input("Enter your selection: ")   # Get the user's selection
    if again == 'y':    # If the user selects 'y', run the task again
        print("Thank you! Returning to the task...\n")  # Display a message
        return task()   # Run the task
    elif again == 'n':  # If the user selects 'n', return to the main menu
            print("Thank you! Returning to the main menu...\n")  # Display a message
    else:   # If the user enters anything other than 'y' or 'n', display an error message and ask the user to try again
        print("You must enter a 'y' or an 'n'!")    # Display an error message
        repeat_task(task)   # Run the function again

def is_correct_task(task): # function to check if the user is on the correct task
    print(f"Is this the corect task? (y/n)") # Ask the user if this is the correct task
    correct_task = input("Enter your selection: ")  # Get the user's selection
    if correct_task == 'y': # If the user selects 'y', start the task
        print("Thank you! Now starting the task...")    # Display a message
        return task()   # Run the task
    elif correct_task == 'n':   # If the user selects 'n', return to the main menu
        print("Thank you! Returning to the main menu...\n")   # Display a message
    else:   # If the user enters anything other than 'y' or 'n', display an error message and ask the user to try again
        print("You must enter a 'y' or an 'n'!")    # Display an error message
        is_correct_task(task)  # Run the function again

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

def run_capitalize(): # function to run the capitalize function
    sentence = input("Enter a sentence: ")    # Get the user's sentence
    capitalized_sentence = capitalize(sentence)    # Capitalize the sentence
    print(f"Here is your capitalized sentence:\n\n'{capitalized_sentence}'")    # Return the capitalized string

def ui_capitalize():    # function to display the user interface for task 1
    print("""
================================================================================================          
*** Welcome to the capitalizer! ***
This task will correctly capitalize a sentece. 
================================================================================================""")
    is_correct_task(run_capitalize) # Check if the user is on the correct task
    repeat_task(run_capitalize) # Check if the user would like to run the task again

""" Task 2: Identify if a string is a palindrome """
def is_palindrom(string): # function to identify if a string is a palindrome
    string = string.lower()    # Convert the string to lower case
    string = re.sub(r'[^a-z]', '', string)    # Remove all non-alphabetical characters
    if string == string[::-1]:    # If the string is equal to the reverse of the string, it is a palindrome
        return True    # Return True
    else:    # If the string is not equal to the reverse of the string, it is not a palindrome
        return False    # Return False

def run_palindrom():
    string = input("Enter a string to check if it is a palindrome: ")   # Get a string from the user
    if is_palindrom(string):    # If the string is a palindrome, display a message to the user
        print(f"{string} is a palindrome!")   # Display a message to the user
    else:
        print(f"{string} is not a palindrome.")
    
def ui_palindrome():    # function to display the user interface for task 2
    # code for user interaction with the palindrome task
    print("""
================================================================================================          
*** Welcome to the palindrome identifier! ***
This task will identify if a string is a palindrome.
================================================================================================
Is this the corect task? Type 'y' for yes or 'n' for no and return to the menu.""")
    is_correct_task(run_palindrom)  # Check if the user is on the correct task
    repeat_task(run_palindrom)  # Check if the user would like to run the task again

""" Task 3: Generate a reverse order freq. list of words in a PDF """
def read_pdf():  # Function to read a pdf file and extract the text
    with open("Neg Inversions_2018.pdf", "rb") as pdf_file_in:  # Open the pdf
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_in)  # Read the pdf
        for page in range(pdf_reader.getNumPages()):    # Get the number of pages in the pdf
            page = pdf_reader.getPage(page)  # Get the page
            text = page.extractText()   # Extract the text from the page
    return text   # Return the text

def tokenize(text):   # Function to tokenize the text into words
    tokens = word_tokenize(text)   # Tokenize the text into words
    return tokens   # Return the tokens

def remove_stopwords(text):   # Function to remove stopwords from the text
    stops = stopwords.words('english')   # Define stopwords to remove from the list
    no_stops = [word for word in text if word not in stops]   # Remove stopwords from the text
    return no_stops   # Return the text without stopwords

def expand_contractions(text) -> list:   # Function to expand contractions
    contractions = {   # Define a dictionary of contractions to expand
        "ain't": "am not","aren't": "are not","can't": "cannot","can't've": "cannot have","'cause": "because",
        "could've": "could have","couldn't": "could not","couldn't've": "could not have","didn't": "did not",
        "doesn't": "does not","don't": "do not","hadn't": "had not","hadn't've": "had not have","hasn't": "has not",
        "haven't": "have not","he'd": "he had","he'd've": "he would have","he'll": "he shall","he'll've": "he shall have",
        "he's": "he has","how'd": "how did","how'd'y": "how do you","how'll": "how will",
        "how's": "how has","i'd": "I had","i'd've": "I would have"
    }
    text = [contractions[word] if word in contractions else word for word in text]   # Expand all contractions in the text
    return text  # Return the text with expanded contractions
        
def clean_text(text) -> list:   # Function to clean the text
    text = [word.lower() for word in text]   # Convert all text to lower case
    text = [re.sub(r'[^a-z]', '', word) for word in text]   # Remove all non-alphabetical characters
    text = [word for word in text if word != '']   # Remove all empty strings
    cleaned_text = text   # Set the cleaned text to the text
    return cleaned_text  # Return the cleaned text

def frequency_list(text):    # Function to create a frequency list of words and sort it in reverse order
    freq_list = {}    # Define an empty dictionary
    for word in text:    # For each word in the text
        if word in freq_list:    # If the word is already in the dictionary
            freq_list[word] += 1    # Increment the count
        else:    # If the word is not in the dictionary
            freq_list[word] = 1    # Add the word and set the count to 1
    freq_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)    # Sort the dictionary in reverse order
    return freq_list    # Return the sorted dictionary

def to_json(freq_list):    # Function to convert the frequency list to a JSON file
    with open("freq_list.json", "w") as f:    # Open the JSON file
        json.dump(freq_list, f)    # Write the frequency list to the JSON file

def run_freq_list():    # Function to run the frequency list task    
    text = read_pdf()    # Read the text from the pdf
    tokens = tokenize(text)    # Tokenize the text
    no_stops = remove_stopwords(tokens)    # Remove stopwords from the text
    expanded = expand_contractions(no_stops)    # Expand contractions in the text
    cleaned_text = clean_text(expanded)    # Clean the text
    freq_list = frequency_list(cleaned_text)    # Create a frequency list of words
    to_json(freq_list)    # Convert the frequency list to JSON
    print("The frequency list has been created and saved as 'freq_list.json!")

def ui_freq_list():    # Function to handle user input for the frequency list task
    print("""
================================================================================================          
*** Welcome to the frequency list task! ***\n
This task will create a frequency list of words in the 
pdf file 'Neg Inversions_2018.pdf' and save it as a JSON file.
================================================================================================""")
    is_correct_task(run_freq_list)    # Run the frequency list task if it is the desired task
    repeat_task(run_freq_list)    # Run the frequency list task again if the user wants to
    
""" Task 4: Pride and Prejudice find similies """
def find_similes(text):
  similes = []
  # Use a regular expression to find similes in the form "X is/was/were/are like/as Y"
  pattern = re.compile(r"\b(\w+) (is|was|were|are) (like|as) (\w+)\b")  # Create a pattern object
  matches = pattern.finditer(text)  # Find all matches in the text
  # Loop through the matches and add the sentences containing the similes to the list
  for match in matches: # Loop through the matches
    # Find the start and end indices of the sentence containing the simile
    start_index = text.rfind(".", 0, match.start()) + 1 # Find the last period before the match
    end_index = text.find(".", match.end()) # Find the next period after the match
    # Add the sentence containing the simile to the list of similes
    similes.append(text[start_index:end_index]) # Add the sentence to the list
  return similes    # Return the list of similes

def open_file():    # Open the file and read the text
    with open("prideprej.txt", "r") as f:   # Open the file
            text = f.read()  # Read the text
            similes = find_similes(text)    # Find the similes
            return similes  # Return the list of similes

def output_file():  # Write the similes to a file
    similes = open_file()  # Open the file and read the text
    with open("similes.txt", "w") as f: # Open the file
        for simile in similes:  # Loop through the similes
            f.write("Simile found: " + str(simile) + "\n")  # Write the simile to the file
        
def ui_pride_and_prejudice():    # Function to handle user input for the pride and prejudice task
    print("""
================================================================================================
*** Welcome to the pride and prejudice task! ***\n
This task will find similes in the text file 'prideprej.txt' and output them to a file.
In efforts to save time, instead of using a more complex method of heuristics to find sililes,
or training a machine learning model to find similes, this task utilizes a regular expression
to find similes in the form "X is/was/were/are like/as Y". This method is not perfect, but it
is a good starting point for finding similes in a text. With more time to dedicate learning how
to train a machine learning model, I would be able to create a more accurate
model to find similes. For now though, regular expressions do a decent job.
================================================================================================""")
    is_correct_task(output_file)    # Run the pride and prejudice task if it is the desired task
    repeat_task(output_file)    # Run the pride and prejudice task again if the user wants to

""" Task 5: Find people listed on the linguistics wikipedia page """
def read_wiki():    # Function to read the text from the wikipedia page
    try:    # Try to read the text from the wikipedia page
        wiki_url = "https://en.wikipedia.org/wiki/Linguistics"    # Define the url
        response = requests.get(wiki_url)    # Get the response from the url
        soup = BeautifulSoup(response.text, "html.parser")    # Create a soup object
        text = soup.get_text()    # Get the text from the soup object
        return text    # Return the text
    except:    # If the text cannot be read
        print("Error reading the text from the wikipedia page")   # Print an error message
        
def get_people(text):    # Function to get the people from the text
    doc = nlp(text)    # Create a spaCy document
    people = []    # Define an empty list
    for ent in doc.ents:    # For each entity in the document
        if ent.label_ == "PERSON":    # If the entity is a person
            people.append(ent.text)    # Append the entity to the list
        else:   # If the entity is not a person
            continue    # Continue to the next entity
    return people    # Return the list

def remove_linguistics(people):   # Function to remove the word linguistics from the list
    people = [person for person in people if person.lower() != "linguistics"]    # Remove the word linguistics from the list
    return people    # Return the list

def people_frequency_list(people):    # Function to create a frequency list of people
    freq_list = {}    # Define an empty dictionary
    for person in people:    # For each person in the list
        if person in freq_list:    # If the person is already in the dictionary
            freq_list[person] += 1    # Increment the count
        else:    # If the person is not in the dictionary
            freq_list[person] = 1    # Add the person and set the count to 1
    freq_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)    # Sort the dictionary in reverse order
    return freq_list    # Return the sorted dictionary

def top_ten_people(freq_list):    # Function to print the top ten people
    print("The top ten people in linguistics are:")
    for i in range(10):    # For the first ten items in the list
        print(f"{i+1}. {freq_list[i][0]}")    # Print the person

def run_people():   # Function to run the people task
    text = read_wiki()    # Read the text from the wikipedia page
    people = get_people(text)    # Get the people from the text
    people = remove_linguistics(people)    # Remove the word linguistics from the list
    freq_list = people_frequency_list(people)    # Create a frequency list of people
    top_ten_people(freq_list)    # Print the top ten people

def ui_people():    # Function to run the people task from the user interface
    print("""
================================================================================================          
*** Welcome to the frequency list task! ***\n
This task will extract all PERSON-type entities from the linguistics 
Wikipedia page and generate a frequency list of those entities.
Along with the frequency list, the top ten people in linguistics will be printed.
================================================================================================""")
    is_correct_task(run_people)   # Run the people task
    repeat_task(run_people)    # Ask the user if they want to repeat the task
    
""" Task 6: Display the dependency parse for the 78th sentence of the linguistics wikipedia page """""
def get_sentence():    # Return the 78th sentence
    wiki = read_wiki()    # Read the text from the wikipedia page
    sentences = sent_tokenize(wiki)    # Tokenize the text into sentences
    return sentences[77]    # Return the 78th sentence
    
def display_dependency_parse(sentence):    # Function to display the dependency parse
    doc = nlp(sentence)    # Create a Doc object from the sentence
    results = []    # Create an empty list to store the results
    for token in doc:    # For each token in the sentence
        result = [token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children]]    # Create a list with the token, dependency, head, head part of speech, and children
        results.append(result)    # Add the result to the list
    df = pd.DataFrame(results, columns=["Token", "Dependency", "Head", "Head POS", "Children"])    # Create a DataFrame from the list of results
    return df    # Return the DataFrame

def run_dependency_parse():    # Function to run the dependency parse task
    sentence = get_sentence()    # Get the 78th sentence
    dependency_parse = display_dependency_parse(sentence)    # Display the dependency parse
    print(dependency_parse)    # Print the dependency parse

def ui_dependency_parse():    # Function to run the dependency parse task from the user interface
    print("""
================================================================================================
*** Welcome to the dependency parse task! ***\n
This task will display the dependency parse for the 78th sentence of the linguistics Wikipedia page.
================================================================================================""")
    is_correct_task(run_dependency_parse)    # Run the dependency parse task
    repeat_task(run_dependency_parse)    # Ask the user if they want to repeat the task
    
""" Task 7: Generate a tree diagram from a hardcoded sentence """
# second attempt at the tree diagram this time using displacy, the original code was unable to run with nltk for some reason
def generate_tree_diagram(sentence):    # Function to generate a tree diagram using displacy
    doc = nlp(sentence)    # Create a spaCy document
    tree = displacy.render(doc, style="dep", jupyter=False)    # Render the tree diagram
    with open("tree.html", "w", encoding="utf-8") as f:   # Write the tree diagram to a file
        f.write(tree)   # Write the tree diagram to the file

def run_tree_diagram():    # Function to run the tree diagram task
    sentence = "John believes that Mary loves him."    # Define the sentence
    generate_tree_diagram(sentence)    # Generate the tree diagram

def ui_tree_diagram():  # Function to display the ui for the tree diagram task
    print("""
================================================================================================
*** Welcome to the tree diagram task ***\n
This task will generate a tree diagram for a hardcoded sentence and output it as 'tree.html'
The sentence is: "John believes that Mary loves him."
================================================================================================""")
    is_correct_task(run_tree_diagram)   # Check if it is the correct task
    repeat_task(run_tree_diagram)   # Ask if the user wants to repeat the task
    
""" Whooooo! Last task! Task 8: Chunk a sentence into all NPs, PPs, and VPs """        
def chunk_sentence(sentence):   # Function to chunk a sentence using NLTK            # I had to look up the grammar for this one
    grammar = r"""           # Define the grammar
NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>}               # Chunk prepositions followed by NP
VP: {<MD>?<VB.*><NP|PP>*}    # Chunk verbs followed by optional modals, NP or PP
"""
    tokens = word_tokenize(sentence)    # Tokenize the sentence
    tagged = nltk.pos_tag(tokens)    # Tag the tokens
    chunker = nltk.RegexpParser(grammar)    # Create a chunker
    chunks = chunker.parse(tagged)    # Parse the tagged tokens
    return chunks    # Return the chunks
    
def run_chunk_sentence():    # Function to run the chunk sentence task
    sentence = input("What sentence do you want to chunk?\n")    # Define the sentence
    chunks = chunk_sentence(sentence)    # Chunk the sentence
    print(chunks)    # Print the chunks
    chunks.draw()    # Draw the chunks

def ui_chunk_sentence():    # Function to display the ui for the chunk sentence task
    print("""
================================================================================================
*** Welcome to the chunk sentence task ***\n
This task will chunk a user inputed sentence into all NPs, PPs, and VPs
================================================================================================""")
    is_correct_task(run_chunk_sentence)
    repeat_task(run_chunk_sentence)

""" Main program loop """ 
def main():   # Main function
    print("\n\n\n*** Welcome to the final project! ***\n")
    mainflag = True  # Set the main flag to true
    while mainflag == True: # While the main flag is true
        menu()  # Call the menu function
        print("Enter a number to select a task or 'q' to quit.")    # Print the menu
        selection = input("Enter your selection: ")   # Get the user's selection
        match selection:    # Match the user's selection
            case '1':   # If the user selected task 1
                ui_capitalize()   # Call the ui_capitalize function
            case '2':   # If the user selected task 2
                ui_palindrome()  # Call the ui_palindrome function
            case '3':   # If the user selected task 3
                ui_freq_list()  # Call the ui_freq_list function
            case '4':   # If the user selected task 3
                ui_pride_and_prejudice()   #  Call the ui_pride_and_prejudice function
            case '5':   # If the user selected task 5
                ui_people()   # Call the ui_people function
            case '6':   # If the user selected task 6
                ui_dependency_parse()   # Call the ui_dependency_parse function
            case '7':   # If the user selected task 7
                ui_tree_diagram()
            case '8':   # If the user selected task 8
                ui_chunk_sentence()   # Call the ui_chunk_sentence function
            case 'q':   # If the user selected to quit
                print("Thank you for using this program! Goodbye!")  # Print a goodbye message
                mainflag = False    # Set the main flag to false
            case _:   # If the user selected an invalid option
                print("Invalid selection. Please try again.")   # Print an error message
                
if __name__ == '__main__':  # If the program is being run directly
    main()  # Call the main function