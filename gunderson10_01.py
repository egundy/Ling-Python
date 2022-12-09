'''
Examine my script for the interrogative conversion. Some blocks of the code are very similar, 
containing repetitive operations. In every step, you make a replacement in the sentence and then 
re-tokenize it. This type of code is wasteful and unclean. 

Your job is to generalize the code, putting repetitive operations in a single function. In doing so, 
you will need to explicitly specify what you are searching for and what operations you want to 
perform on it by either replacing it with another token or adding a token before it.
'''
# imports
import spacy

# Repetitive code that can be put into a function
def convert_to_question(doc, searching_for, replacing_with, adding_before):
  for i,token in enumerate(doc):
    if token.tag_ == searching_for:
      if replacing_with == '': #if there is no replacement, add a token before
        sent = doc[:i].text + ' ' + adding_before + ' ' + doc[i:].text
      else: #if there is a replacement, replace the token
        sent = doc[:i].text + ' ' + replacing_with + ' ' + doc[i+1:].text
      break
  return sent
    
def main():
    # create chatbot that can reconfigure statemenets into questions
    # imports
    nlp = spacy.load('en_core_web_sm')
    doc = nlp("I can promise it is worth your time.")
    sent = ''
    # change to "Can I promise it is worth your time."
    sent = convert_to_question(doc, 'PRP', '', 'Can')
    # re-tokenize
    doc = nlp(sent)
    # change to 'Can you promise it is worth your time.'
    sent = convert_to_question(doc, 'PRP', 'you', '')
    # re-tokenize
    doc = nlp(sent)
    # change to 'Can you promise it is worth my time.'
    sent = convert_to_question(doc, 'PRP$', 'my', '')
    # re-tokenize
    doc = nlp(sent)
    # change to 'Can you really promise it is worth my time.'
    sent = convert_to_question(doc, 'VB', '', 'really')
    # re-tokenize
    doc = nlp(sent)
    # change to 'Can you really promise it is worth my time?'
    sent = doc[:len(doc)-1].text + '?'
    print(sent) 
    
if __name__ == '__main__':
    main()
    
# this program is working, but slightly incorrectly as the final question contains two "Can"s. How can this be fixed?