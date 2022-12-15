import re
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

def main():
    output_file()

if __name__ == "__main__":
    main()
