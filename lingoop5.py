class Speech:
    def __init__(self, s, p):
        self.spelling = s
        self.pronunciation = p
        
    def spell(self):
        return self.spelling
    
    def pronounce(self):
        return self.pronunciation

class Syllable(Speech):
    pass
class Onset(Speech):
    pass
class Nucleus(Speech):
    pass
class Coda(Speech):
    pass
class Rhyme(Speech):
    pass
class Segment(Speech):
    def __init__(self, s, p):
        super().__init__(s, p)
