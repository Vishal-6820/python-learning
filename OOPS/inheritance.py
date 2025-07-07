# inheritance
# class car blueprint

class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def driving(Self):
        print("The car is driving")

# Audi car is inheriting from Car class
class Audi(Car):
     def __init__(self, windows, doors, enginetype, horsepower):
        super().__init__(windows, doors, enginetype)
        self.horsepower = horsepower

     def selfdriving(self):
        print("The Audi is self-driving")    


audiq7 = Audi(4, 5, "Petrol", 300)

print(audiq7.windows)
print(audiq7.horsepower)
audiq7.driving()
audiq7.selfdriving()
