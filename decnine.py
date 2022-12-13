import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Jane Roe meet with the president at the faculty union.")

# define extract_information function
def extract_information(doc):
    # create variables
    action = ''
    participant1 = ''
    participant2 = ''
    for token in doc:
        if (token.lemma_ == 'meet' and token.pos_ == 'VERB' and token.dep_ == 'ROOT'):
            action = token.text
            children = [child for child in token.children]
            for child1 in children:
                if child1.dep_ == 'nsubj':
                    participant1 = ' '.join([attr.text for attr in child1.children]) + ' ' + child1.text
                elif child1.text == 'with':
                    action += ' ' + child1.text
                    child1_children = [child for child in child1.children]
                    for child2 in child1_children:
                        if (child2.pos == 'NOUN'):
                            participant2 = ' '.join([attr.text for attr in child2.children]) + ' ' + child1.text
                elif (child1.dep_ == 'dobj' and child1.pos_ == 'NOUN' or child1.pos_ == 'PROPN'):
                    participant2 = ' '.join([attr.text for attr in child1.children]) + ' ' + child1.text
    print(f"Participant1 = {participant1}")
    print(f"Action = {action}")
    print(f"Participant2 = {participant2}")


extract_information(doc)