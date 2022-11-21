class MyGrandparent:
    info = "I am a grandparent" # class variable
    def hmm(self, x):
        self.oh = x # instance variable
        
class MyParent(MyGrandparent):
    pass
    # create an instatnce method with argument
    def huh(self,x):
        self.huh = x
        print(x)
        
class MyChild(MyParent):
    pass
# create instance of MyChild
a = MyChild()
print(a.info)
a.hmm("bummer")
print(a.oh)
a.huh("doh")