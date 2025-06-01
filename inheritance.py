#inheritance
#inheritance is the process of defining a new class(subclass or derived class) based on an existing class(super class or base class)
# A Cat is a Animal
# A Car is a Vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Starting the vehicle...")

    def stop(self):
        print("Stopping the vehicle...")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors, num_wheels):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.num_wheels = num_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, num_wheels):
        super().__init__(brand, model, year)
        self.num_wheels = num_wheels


car = Car("Toyota", "Camry", 2020, 4, 4)
bike = Bike("Yamaha", "MT-07", 2021, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.start()
car.stop()
bike.stop()
