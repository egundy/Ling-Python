"""Finally, you will create the Zoo object. It will contain cage objects, and they in turn will contain 
animals. The Zoo class need to support the following operations. 

1. Given a zoo z, you should be able to print all the cages (with their ID numbers) and the 
animals inside simply by invoking print(z).

2. You should be able to get the animals with a particular color by invoking the method 
z.animals_by_color('black'). The result should be a list of Animal objects.

3. You should be able to get the animals with a particular number of legs by invoking the method 
z.animal_by_legs. For example, we can get all of the four-legged animals by invoking 
z.animals_by_legs(4). The result should be a list of Animal objects.

4. You have a potential donor to our zoo who wants to provide socks for all of the animals. Thus, 
we need to be able to invoke z.number_of_legs() and get a count of the total number of 
legs for all animals in your zoo. """

from gunderson9_02 import *
# create a class called Zoo
class Zoo():
    # initialize the class
    def __init__(self) -> None:
        pass
    # add more cages to the zoo
    def add_cage(self, cage):
        self.cages.append(cage)
        print("The cage", self.cage, "has been added to the zoo.")
    # remove cages from the zoo
    def remove_cage(self, cage):
        self.cages.remove(cage)
        print("The cage", self.cage, "has been removed from the zoo.")
    # print the cages in the zoo
    def print_cages(self):
        print("The cages in the zoo are", self.cages)
    # print the animals in the zoo
    def print_animals(self):
        print("The animals in the zoo are", self.animals)
    # get all animals with the same color
    def same_color(self, color):
        return [animal for animal in self.animals if animal.color == color]
    # get all animals with the same number of legs
    def animals_by_legs(self, legs):
        return [animal for animal in self.animals if animal.legs == legs]
    # sum the total amount of legs
    def number_of_legs(self):
        return sum([animal.legs for animal in self.animals])
    