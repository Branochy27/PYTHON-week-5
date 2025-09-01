class Smartphone:
    def __init__(self, brand, model, os):
        self.brand = brand
        self.model = model
        self.os = os
        self._battery_level = 100  # Protected attribute

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on...")

    def check_battery(self):
        print(f"Battery level: {self._battery_level}%")

    def charge(self, amount):
        self._battery_level = min(100, self._battery_level + amount)
        print(f"Charging... Battery now at {self._battery_level}%")

     #b. subclass
        
class Samsung(Smartphone):
    def __init__(self, model, os, fingerprint_enabled):
        super().__init__("Samsung", model, os)
        self.__fingerprint_enabled = fingerprint_enabled  # Private attribute

    def unlock(self):
        if self.__fingerprint_enabled:
            print(f"{self.model} unlocked with fingerprint.")
        else:
            print(f"{self.model} unlocked with PIN.")

    # Polymorphism: override power_on
    def power_on(self):
        print(f"Samsung {self.model} boots with One UI on {self.os}.")

#example in real world
galaxy = Samsung("Galaxy S22", "Android 13", True)
galaxy.power_on()         # Polymorphic behavior
galaxy.check_battery()    # Inherited method
galaxy.charge(15)         # Encapsulated battery logic
galaxy.unlock()           # Encapsulated fingerprint logic





#question 2     polymorphism with Vehicles

class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the water 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling down the lane 🚴")                