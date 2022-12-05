import spaCy
from spacy.symbols import ORTH, LEMMA
nlp = spacy.load('en_core_web_sm')
doc = nlp("I am flying to Frisco.")
print([w.text for w in doc])

# Identify the orthographic "Frisco"'s actual lemma is San Francisco
# Then save it as a special case
special_case = [{ORTH: "Frisco", LEMMA: "San Francisco"}]

# Let's add the special case to the tokenizer

nlp.tokenizer.add_special_case("Frisco", special_case)

# Now let's see the result
print([w.lemma_ for w in nlp('I am flying to Frisco.')])