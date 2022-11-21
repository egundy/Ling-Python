#create a class for exceptions that will be raised when the parser encounters an error
class ParserError( Exception ): 
    pass    #pass as a null statement. this allows the class to be created without any code in it and use it to return customized error messages

# create a class for the sentence object
class Sentence():
    # initialize the object self and parts of speech list
    def __init__(self, subjecthead, verb, objecthead) -> None:
        self.subjecthead = subjecthead[1]
        self.verb = verb[1]
        self.objecthead = objecthead[1]
    
    # peek at the next word in the list    
    def peek(word_list):
        # if the list is not empty, return the first word in the list
        if word_list:
            word = word_list[0]
            return word[0]
        # if the list is empty, return None
        else:
            return None
    
    # match the word type to the word in the list    
    def match(word_list, expecting):
        # if the list is not empty, return the first word in the list
        if word_list:
            # pop the first word in the list
            word = word_list.pop(0)
            # if the word type matches the word in the list, return the word
            if word[0] == expecting:
                return word
            # else, return None
            else:
                return None
        # if the list is empty, return None
        else:
            return None
        
    # skip the word type in the list        
    def skip(word_list, word_type):
        # while the list is not empty, and the word type matches the word in the list
        while Sentence.peek(word_list) == word_type:
            # match the word type to the word in the list
            Sentence.match(word_list, word_type)
    
    # parse the verb in the list
    def parse_verb(word_list):
        # skip the word type 'det' in the list
        Sentence.skip(word_list, 'det')
        # if the word type is 'verb' 
        if Sentence.peek(word_list) == 'verb':
            # match the word type to the word in the list
            return Sentence.match(word_list, 'verb')
        # else, raise an error
        else:
            raise ParserError("Expected a verb next.")
    
    # parse the object in the list    
    def parse_object(word_list):
        # skip the word type 'det' in the list
        Sentence.skip(word_list, 'det')
        # peek at next word in the list
        next_word = Sentence.peek(word_list)
        # if the word type is 'noun'
        if next_word == 'noun':
            # return the word in the list
            return Sentence.match(word_list, 'noun')
        # else, if the next word is an adverb
        elif next_word == 'adverb':
            # return the word in the list
            return Sentence.match(word_list, 'adverb')
        # else, raise an error
        else:
            raise ParserError("Expected a noun or an adverb next.")
    
    # parse the subject in the list       
    def parse_subjecthead(word_list):
        # skip the word type 'det' in the list
        Sentence.skip(word_list, 'det')
        # peek at next word in the list
        next_word = Sentence.peek(word_list)
        # if the word type is 'noun'
        if next_word == 'noun':
            # return the word in the list
            return Sentence.match(word_list, 'noun')
        # else, if the next word is a verb
        elif next_word == 'verb':
            # return noun and speaker
            return ('noun', 'speaker')
        # else, raise an error
        else:
            raise ParserError("Expected a noun or verb next.")
    
    # parse a sentence in the list    
    def parse_sentence(word_list):
        # parse the subject in the list
        subj = Sentence.parse_subjecthead(word_list)
        # parse the verb in the list
        verb = Sentence.parse_verb(word_list)
        # parse the object in the list
        obj = Sentence.parse_object(word_list)
        
        # return the sentence with the subject, verb, and object
        return Sentence(subj, verb, obj)