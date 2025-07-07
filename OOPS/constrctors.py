class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
            self.species = "Unknown"
            self.age = 0
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
            self.age = 0
        elif len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]  
        else:
            raise ValueError("Invalid number of arguments provided")    

    # def __init__(self, name, species):
    #     self.name = name
    #     self.species = species

    # def __init__(self, name, species, age): 
    #     self.name = name
    #     self.species = species
    #     self.age = age

    def make_sound(self, sound):
        return "The animal is {} and says {}".format(self.name, sound)
    

dog = Animal("Buddy", "Dog", 8)
# cat = Animal("Whiskers", "Cat", 3)


print(dog.name)
print(dog.species)
print(dog.age)