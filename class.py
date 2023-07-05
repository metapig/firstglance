'''
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name)

my_res = Restaurant("iu","Chinese")

my_res.describe_restaurant()
'''
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        if mileage>self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Invalid Operation!")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles



class Battery:
    def __init__(self,battery_size = 75) :
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full range." )

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def system_check(self):
        if self.battery.battery_size >= 20 :
            print("Normal State.")
        else :
            print("Charge your battery!")

    def increment_odometer(self, miles):
        print("The value is fixed!") 


my_byd = ElectricCar("BYD","dolphin",2022)
my_byd.battery.get_range()
my_byd.battery.upgrade_battery()
my_byd.battery.get_range()


















