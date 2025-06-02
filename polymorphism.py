# This is the ability of an object to take on many forms.
## In Python, polymorphism allows methods to do different things based on the object it is acting upon.


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('Vehicle starting...')
    
    def stop(self):
        print('Vehicle stopping...')


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def start(self):
        print('Car starting with a vroom...')
    
    def stop(self):
        print('Car stopping with a screech...')

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
    
    def start(self):
        print('Motorcycle starting with a roar...')

    def stop(self):
        print('Motorcycle stopping with a skid...')


#create a list of vehicles to inspect

vehicles = [
    Car("Toyota", "Camry", 2020, 4),
    Motorcycle("Harley-Davidson", "Street 750", 2019)
]

for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} (type: {type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Unknown vehicle type")