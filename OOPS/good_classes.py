class Car:
    #constructor
    def __init__(self,windows, tyres, engine): 
        self.windows = windows
        self.tyres = tyres
        self.engine = engine

    def self_driving(self, engine):
        print("The car is self-driving with engine type: {}".format(engine))

car1 = Car(4, 4, 'Diesel')
car2 = Car(6, 6, 'Petrol')

print(car1.engine)
print(car2.engine)
print("The no. of tyres in object car1 is: {}".format(car1.tyres))
print("The no. of windows in object car1 is: {}".format(car1.windows))
car1.self_driving("Electric")
