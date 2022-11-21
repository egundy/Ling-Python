class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting")
    
    def rollover(self):
        print(self.name.title() + " rolled over") 
        
    def find_oldest(dogs):
        doggie_ages = []
        for d in dogs:
            doggie_ages.append(d.age)
        doggie_ages.sort(reverse=True)
        print("The oldest dog is:", doggie_ages[0], "years old.")
        
charlie = Dog("Charlie", 5)
fido = Dog("Fido", 3)
rex = Dog("Rex", 8)
dogs = [charlie, fido, rex]

"""Run the find_oldest method on the list of dogs"""
Dog.find_oldest(dogs)

"""Run the sit method on the list of dogs"""
