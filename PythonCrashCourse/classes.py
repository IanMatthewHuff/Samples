class Dog():
    """ A simple dog model """

    def __init__(self, name, age):
        """ Initialize attributes """
        self.name = name
        self.age = age

    def sit(self):
        """ Dog is now sitting """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ Roll over """
        print(self.name.title() + " just rolled over!")

#  __init__() is alwasy the constructor method, self is required as the first parameter
# self is automatically passed so we just need to call the constructor with name and age
# variables assigned to self are attributes

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print("Your dog's name is " + your_dog.name.title() + ".")
your_dog.sit()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has driven " + str(self.odometer) + " miles.")

    def update_odometer(self, miles):
        if (miles >= self.odometer):
            self.odometer = miles
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(50)
my_new_car.read_odometer()
my_new_car.update_odometer(25)
my_new_car.increment_odometer(25)
my_new_car.read_odometer()

# Inheritence
# __init__ in child class needs help from parent class

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery.")

    # This is how you can override a parnet class method
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery.")

class ElectricCar2(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        self.battery.describe_battery()

    # This is how you can override a parnet class method
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

# super() makes the connection to the parent class
# note that this is different in Python 2.7

tesla2 = ElectricCar2('tesla', 'model x', 2018)
tesla2.describe_battery()

# Importing - say that we put the car class into a file car.py
# we can put a module level docstring in at that point
# then in our file use "from car import Car" to bring in the class

# You can store multiple classes in a module
# "from car import Car, ElectricCar

# Can import an entire module. Adds a module namespace when you do this
# import car
# car.Car('volkswagen', 'beetle', 2016)


