'''My chatbot code does not work for many sentences. The script adds “do” to form a question, 
which works only with sentences that contain no auxiliar verb. Enhance the functionality of this 
script so it can also work with sentences containing modal verbs. For example, given the 
following statement, “I might want a green apple.” the script should generate “Why might you 
want a green one?”'''
# create chatbot that can reconfigure statemenets into questions
# imports
import spacy

# function that finds the direct object in a sentence
def find_chunk(doc):
    for i, token in enumerate(doc):
        if token.dep_ == 'dobj':
            shift = len([w for w in token.children])
            chunk = doc[i-shift:i+1]
            break
    print("chunk found")
    return chunk

# function that determines the question type
def determine_question_type(chunk):
    question_type = 'yesno'
    for token in chunk:
        if token.dep_ == 'amod':
            question_type = 'info'
    print("question type determined")
    return question_type

# function that determines if there is a modal verb in the sentence
def find_modal(doc):
    for token in doc:
        if token.pos_ == 'VERB' and token.tag_ == 'MD':
            return True
    return False

# function that generates the question
def generate_question(nlp, doc, question_type):
    sent = ''
    print("generating question")
    for i, token in enumerate(doc):
        if token.tag_ == 'PRP' and doc[i+1].tag_ == 'VBP':
            sent = 'do ' + doc[i].text
            sent = sent + ' ' + doc[i+1:].text
            break
    doc = nlp(sent)
    for i, token in enumerate(doc):
        if token.tag_ == 'PRP' and token.text == 'I':
            sent = doc[:i].text + ' you ' + doc[i+1:].text
            print(sent)
            break
    doc = nlp(sent)
    if question_type == 'info':
        for i, token in enumerate(doc):
            if token.dep_ == 'dobj':
                sent = 'why ' + doc[:i].text + ' one ' + doc[i+1:].text
                print(sent, ": info question")
                break
    elif 'yesno':
        sent = 'do you ' + doc.text
    else:
        raise ValueError('Invalid question type')
    doc = nlp(sent)
    # add a question mark
    # capitalize the first letter
    sent = sent[0].upper() + sent[1:] + '?'
    print(sent)
    return sent

# the main code
def main():
    # load the small English model
    nlp = spacy.load('en_core_web_sm')
    # get the sentence from the command line
    sentence = "I might want a green apple."
    # parse the sentence
    doc = nlp(sentence)
    # find the chunk
    chunk = find_chunk(doc)
    # determine the question type
    question_type = determine_question_type(chunk)
    # determine if there is a modal verb
    # generate the question
    generate_question(nlp, doc, question_type)
    # print the question

if __name__ == '__main__':
    main()
    
# this code doesn't work properly and I cannot figure out why. Instead of printing what it is supposed to print, it just prints an empty line