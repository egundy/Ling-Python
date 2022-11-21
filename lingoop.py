class Dog:
    
    species = "canis familiaris"
    sound = "woof"
    def __init__(self, name, age, breed, sex) -> None:
        self.name = name
        self.age = age
        self.breed = breed
        self.sex = sex
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self):
        return f"{self.name} says {self.sound}"


charlie = Dog("Charlie", 5, "Golden Doodle", "M")
bob = Dog("Bob", 6, "Sheepadoodle", "M")
charlie.sound = "bow wow"