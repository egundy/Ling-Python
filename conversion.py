import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("I can promise it is worth your time.")
sent = ''
for i,token in enumerate(doc):
 if token.tag_ == 'PRP' and doc[i+1].tag_ == 'MD' and doc[i+2].tag_ == 'VB':
   sent = doc[i+1].text.capitalize() + ' ' + doc[i].text
   sent = sent + ' ' + doc[i+2:].text
   break
#By now, you should have: 'Can I promise it is worth your time.'

#Retokenization
doc=nlp(sent)
for i,token in enumerate(doc):
  if token.tag_ == 'PRP' and token.text == 'I':
    sent = doc[:i].text + ' you ' + doc[i+1:].text
    break
#By now, you should have: 'Can you promise it is worth your time.'

doc=nlp(sent)
for i,token in enumerate(doc):
  if token.tag_ == 'PRP$' and token.text == 'your':
    sent = doc[:i].text + ' my ' + doc[i+1:].text
    break
#By now, you should have: 'Can you promise it is worth my time.'

doc=nlp(sent)
for i,token in enumerate(doc):
  if token.tag_ == 'VB':
    sent = doc[:i].text + ' really ' + doc[i:].text
    break
#By now, you should have: 'Can you really promise it is worth my time.'

doc=nlp(sent)
sent = doc[:len(doc)-1].text + '?'
#Finally, you should have: 'Can you really promise it is worth my time?'

print(sent)

'''Your job is to generalize the code, putting repetitive operations in a single function. In doing so, 
you will need to explicitly specify what you are searching for and what operations you want to 
perform on it by either replacing it with another token or adding a token before it.'''

# generalized function that specifies what to search for and what operations to perform
def convert_to_question(searching_for, replacing_with, adding_before):
  doc = nlp(sent)
  for i,token in enumerate(doc):
    if token.tag_ == searching_for:
      if replacing_with == '': #if there is no replacement, add a token before
        sent = doc[:i].text + ' ' + adding_before + ' ' + doc[i:].text
      else: #if there is a replacement, replace the token
        sent = doc[:i].text + ' ' + replacing_with + ' ' + doc[i+1:].text
      break
  return sent

