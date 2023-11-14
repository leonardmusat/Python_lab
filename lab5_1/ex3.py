class Vehicle:
    def __init__(self, mass, hp, max_speed, make, tank, consumption):
        self.mass = mass
        self.make = make
        self.hp = hp
        self.max_speed = max_speed
        self.tank = tank
        self.consumption = consumption

    def mileage(self):
        return self.tank / self.consumption


class Truck(Vehicle):
    def __init__(self, mass, hp, max_speed, make, tank, consumption, tow_mass):
        Vehicle.__init__(self, mass, hp, max_speed, make, tank, consumption)
        self.tow_mass = tow_mass

    def towing_capacity(self):
        return 100*(self.hp * 756 * 2)/(self.max_speed * self.max_speed) - self. mass - self.tow_mass


class Car(Vehicle):
    def __init__(self, mass, hp, max_speed, make, tank, consumption):
        Vehicle.__init__(self, mass, hp, max_speed, make, tank, consumption)

    def towing_capacity(self):
        return 100*(self.hp * 756 * 2) / (self.max_speed * self.max_speed) - self.mass


class Motorbike(Vehicle):
    def __init__(self, mass, hp, max_speed, make, tank, consumption):
        Vehicle.__init__(self, mass, hp, max_speed, make, tank, consumption)


    def towing_capacity(self):
        print("Do not attach a tow to a motorbike!!")


car = Car(500, 75, 140, "Logan", 50, 5)
print("This car is a ", car.make, " with a mileage of ", car.mileage() , "and a towing capacity of", car.towing_capacity())
truck = Truck(2000, 600, 90, "Volvo", 200, 20, 700)
print("This car is a ", truck.make, " with a mileage of ", truck.mileage() , "and a towing capacity of", truck.towing_capacity())
motorbike = Motorbike(100, 50, 120, "Suziki", 20, 4)
print("This car is a ", motorbike.make, " with a mileage of ", motorbike.mileage() , "and a towing capacity of", motorbike.towing_capacity())

