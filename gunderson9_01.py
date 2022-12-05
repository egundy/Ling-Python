"""
Assignment 8:

Let's assume that we are creating a Zoo that contains four different types of animals: 
sheep, wolves, snakes, and parrots. First, create classes for each of these types, such that we can print 
each of them and get a report on their colors, species, and number of legs. 
To give you a hint, you may consider creating the five classes: Animal, Wolf, Sheep, Snake, and Parrot. 
The Animal class should include the __repr__ method, which produce appropriate output (color, species, 
and the number of legs). Note that the function of the __repr__ method is to return a printable 
representation of an object. For example, the __repr__ method in the Animal class below 
returns the string “You just called __repr__”"""


#create the superclass called Animal
class Animal:
    def __init__(self, color, species, legs):
        self.color = color
        self.species = species
        self.legs = legs
    def __repr__(self):
        print("a", self.color, self.species, "with", self.legs, "legs.")
        return "You just called __repr__"
    
# create a subclass called Wolf
class Wolf(Animal):
    def __init__(self, color, species, legs):
        Animal.__init__(self, color, species, legs)
        
    color = "grey"
    species = "wolf"
    legs = 4
    
# create a subclass called Sheep
class Sheep(Animal):
        def __init__(self, color, species, legs):
            Animal.__init__(self, color, species, legs)
            
        color = "white"
        species = "sheep"
        legs = 4

# create a subclass called Snake
class Snake(Animal):
        def __init__(self, color, species, legs):
            Animal.__init__(self, color, species, legs)
            
        color = "green"
        species = "snake"
        legs = 0
        
# create a subclass called Parrot
class Parrot(Animal):
        
        def __init__(self, color, species, legs):
            Animal.__init__(self, color, species, legs)
            
        color = "red"
        species = "parrot"
        legs = 2


""" Main function to call the classes """
def main():
    wolf = Wolf("grey", "Canis lupus", 4)
    sheep = Sheep("white", "Ovis aries", 4)
    snake = Snake("green", "Python regius", 0)
    parrot = Parrot("red", "Psittacus erithacus", 2)
    
    print(wolf)
    print(sheep)
    print(snake)
    print(parrot)

#run main function    
if __name__ == "__main__":
    main()