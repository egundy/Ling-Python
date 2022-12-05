from gunderson9_01 import *

"""Second, let's put the animals into cages. To do so, you need to create a Cage class, into which 
you can put one or more animals. When you create a new Cage, you will give it a unique ID 
number. You also need to define a __repr__ method so that printing a cage prints not just the cage ID, 
but also each of the animals it contains. """

# create a class called Cage
class Cage():
    # initialize the class
    def __init__(self, cage_id, animal) -> None:
        self.cage_id = cage_id
        self.animal = animal
        self.animals = []
        
    # define the __repr__ method
    def __repr__(self):
        return(f"The cage ID is {self.cage_id} and the animals are {self.animal}")
        
    
    # define the add_animal method
    def add_animal(self, animal):
        self.animals.append(animal)
        print("The animal", self.animal, "has been added to the cage.")

    # define the remove_animal method
    def remove_animal(self, animal):
        self.animal = animal
        self.animals.remove(animal)
        print("The animal", self.animal, "has been removed from the cage.")
        
    # define the print_animals method
    def print_animals(self):
        print("The animals in the cage are", self.animals)  