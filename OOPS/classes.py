# Classes
# Constructors, attributes, methods


# Classes : Classes are real-world enity and object. inside diff diff attributes and methods
# Attributes : Attributes are the properties of the class. They are used to store data.
# Methods : Methods are the functions of the class. They are used to perform actions on the data.

class Car:
    pass

car1 = Car()
car2 = Car()

car1.windows = 4
car1.tyres = 4
car1.engine = 'Desel'

car2.windows = 6
car2.tyres = 6
car2.engine = 'Petrol'

print(car1.engine)
print(car2.engine)
print(dir(car1))
       