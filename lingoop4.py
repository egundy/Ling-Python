class MyMom:
    info = "I am a mom"
    #instance method
    def mySet(self, x):
        self.oh = x
        print(x)
    
class MyDad:
    info = "I am a dad"
    #instance method
    def __init__(self, x) -> None:
        self.var = x

class MyChild(MyMom, MyDad):
    pass

# make an instance of MyChild
a = MyChild('hello')
#istance method from MyMom
a.mySet('hi')
#class variable from MyMom
print(MyChild.info)
#instance variable from MyDad
print(a.var)
#instance variable from MyMom
print(a.info)