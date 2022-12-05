"""
* First, create a class called Dishes, which has the property of outputting the name of the dish and 
    the main nutrient in the dish. 
* Then, create three child classes of Dishes, called Main, Side, and Dessert. 
    Each of these should be created with a name and their main nutrient; make the default 
    nutrient of Dessert be “none.” 
* Next, create a Plate class. Each Plate should have three dishes on 
    it, though they can be any type of dish. You need to write methods to find out if a plate is mom-
    approved and kid-approved. A mom will approve of a plate if there is a main dish and no more 
    than one dessert, and a kid will approve of a plate if there is at least one dessert on the plate. 
* Finally, create a Table class. Each Table should be able to have any number of Plates put on it. 
    You should also make it so that when you print the Table, it prints each Plate with the Plate's 
    Dishes on it. You also need to see what nutrients are at each table, so create a method that, when 
    you call it, will output a list of all of the nutrients at the table with no repetition (“none” counts 
    as a nutrient). 
    """

# Create a class called Dishes, outputting the name of the dish and the main nutrient in the dish
class Dishes:
    def __init__(self, name, nutrient):
        self.name = name
        self.nutrient = nutrient

    def __str__(self):
        return f"{self.name} has a main nutrient {self.nutrient}."
    
# Create three child classes of Dishes, called Main, Side, and Dessert
class MainDish(Dishes):
    def __init__(self, name, nutrient):
        super().__init__(name, nutrient)
    def __str__(self):
        return f"{self.name}"

class SideDish(Dishes):
    def __init__(self, name, nutrient):
        super().__init__(name, nutrient)
    def __str__(self):
        return f"{self.name}"

class Dessert(Dishes):
    def __init__(self, name, nutrient="none"):
        super().__init__(name, nutrient)
    def __str__(self):
        return f"{self.name}"

# Create a Plate class with three dishes on it. Need to find out if a plate is mom-approved and kid-approved
class Plate():
    def __init__(self, dish1, dish2, dish3):
        self.dish1 = dish1
        self.dish2 = dish2
        self.dish3 = dish3
    # how plates are printed
    def __str__(self):
        return f"{self.dish1}, {self.dish2}, and {self.dish3}\n"
    # method to find out if a plate is mom-approved
    def mom_approved(self):
        if isinstance(self.dish1, MainDish) and isinstance(self.dish2, Dessert) and isinstance(self.dish3, Dessert):
            return True
        else:
            return False
    # method to find out if a plate is kid-approved
    def kid_approved(self):
        if isinstance(self.dish1, Dessert) or isinstance(self.dish2, Dessert) or isinstance(self.dish3, Dessert):
            return True
        else:
            return False
    # method to find out what nutrients are on the plate
    def nutrients(self):
        nutrients = []
        if self.dish1.nutrient not in nutrients:
            nutrients.append(self.dish1.nutrient)
        if self.dish2.nutrient not in nutrients:
            nutrients.append(self.dish2.nutrient)
        if self.dish3.nutrient not in nutrients:
            nutrients.append(self.dish3.nutrient)
        return nutrients
    
# Create a Table class. Each Table should be able to have any number of Plates put on it
class Table():
    def __init__(self, *plates):
        self.plates = plates
    # how tables are printed
    def __str__(self):
        table = ""
        for plate in self.plates:
            table += f"{plate}"
        return table
    # method to find out what nutrients are at each table with no repetition ("none" counts as a nutrient)
    def nutrients(self):
        nutrients = []
        for plate in self.plates:
            for nutrient in plate.nutrients():
                if nutrient not in nutrients:
                    nutrients.append(nutrient)
        return nutrients

# main function
def main():
    # create dishes
    steak = MainDish("steak", "protein")
    potatoes = SideDish("potatoes", "carbs")
    cake = Dessert("cake")
    # create plates
    plate1 = Plate(steak, potatoes, cake)
    plate2 = Plate(cake, cake, cake)
    plate3 = Plate(steak, cake, potatoes)
    # create tables
    table1 = Table(plate1, plate2, plate3)
    table2 = Table(plate1, plate2)
    # print tables
    print(table1)
    print(table2)
    print()
    # print nutrients at each table
    print(table1.nutrients())
    print(table2.nutrients())
    print()
    # print mom-approved plates
    print(plate1.mom_approved())
    print(plate2.mom_approved())
    print(plate3.mom_approved())
    print()
    # print kid-approved plates
    print(plate1.kid_approved())
    print(plate2.kid_approved())
    print(plate3.kid_approved())
    print()

# call main function
if __name__ == "__main__":
    main()