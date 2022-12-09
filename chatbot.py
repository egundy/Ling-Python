# imports
import spacy
import sys
# function to find the chunk of the sentence that contains the direct object
def find_chunk(doc):
  # set the chunk to an empty string
  chunk = ''
  # loop through the tokens in the sentence
  for i,token in enumerate(doc):
    # if the token is a direct object
    if token.dep_ == 'dobj':
      # set the shift to the number of children of the token
      shift = len([w for w in token.children])
      # set chunk to the sentence from the token to the token plus the number of children
      chunk = doc[i-shift:i+1]
      # break the loop
      break
  # return the chunk
  return chunk  
# function to determine the question type
def determine_question_type(chunk):
  # set the question type to yesno
  question_type = 'yesno'
  # loop through the tokens in the chunk
  for token in chunk:
    # if the token is an adjective modifier
    if token.dep_ == 'amod':
      # set the question type to info
      question_type = 'info'
  return question_type

# what the below code does is it takes a sentence and turns it into a question
def generate_question(doc, question_type):
  sent = ''
  nlp = spacy.load('en_core_web_sm')
  for i,token in enumerate(doc):
    if token.tag_ == 'PRP' and doc[i+1].tag_ == 'VBP':
      sent = 'do ' + doc[i].text
      sent = sent + ' ' + doc[i+1:].text
      break
  doc=nlp(sent)
  for i,token in enumerate(doc):
    if token.tag_ == 'PRP' and token.text == 'I':
      sent = doc[:i].text + ' you ' + doc[i+1:].text
      break
  doc=nlp(sent)
  if question_type == 'info':
    for i,token in enumerate(doc):
      if token.dep_ == 'dobj':
        sent = 'why ' + doc[:i].text + ' one ' + doc[i+1:].text
        break
  if question_type == 'yesno':
    for i,token in enumerate(doc):
      if token.dep_ == 'dobj':
        sent = doc[:i-1].text + ' a red ' + doc[i:].text
        break
  doc=nlp(sent)
  sent = doc[0].text.capitalize() +' ' + doc[1:len(doc)-1].text + '?'
  return sent
#the main code
def main():
  sent = "I might want to eat a green apple."
  nlp = spacy.load('en_core_web_sm')
  doc = nlp(sent)
  chunk = find_chunk(doc)
  if str(chunk) == '':
    print('The sentence does not contain a direct object.')
    sys.exit()
  question_type = determine_question_type(chunk)
  question = generate_question(doc, question_type)
  print(question)
if __name__ == '__main__':
  main()

# what does the above code do?
# 1. It takes a sentence as input.
# 2. It finds the direct object in the sentence.
# 3. It determines the question type (yesno or info).
# 4. It generates a question based on the question type.
# 5. It prints the question.
# 6. It exits.

# Simplify the code above by using the following functions: 