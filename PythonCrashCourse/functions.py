def greet_user():
    """display a simple greeting."""
    print("Hello!")

greet_user()

def greet_user2(username):
    print("Hello, " + username.title() + "!")

greet_user2("Ian")
greet_user2("Liz")

# Positional arguments are called by position in the function
def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
# We need to provide an animal type and a name in that order

# Keyword argument is a name -> value pair that we pass
describe_pet(animal_type='hamster',pet_name='Franco')
describe_pet(pet_name='reepy',animal_type='pig')
# order can be swapped

def add_one(value=1):
    value += 1

add_one(5)
add_one()
# As you would expect default parameters need to come after required parameters

def get_formatted_name(first_name, last_name):
    """Return a formatted full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name2(first_name, last_name, middle_name=''):
    """Return formatted full name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name2('john','hooker','lee')
print(musician)
# Non empty strings evaluate as True

# More complex data types can be returned
def build_person(first_name, last_name, age=''):
    """Return a dictionary of info about a person"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('frank','sinatra',54)
print(musician)

def greet_users(names):
    """Print a simple greeting"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

# Function can modify the list (reference inside it)
unprinted_designs = ['iphone case','robot pendant','dice']
completed_models = []

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# What if we don't want a list to be modified?
# Just use the slice notation to return a copy
print_models(unprinted_designs[:], completed_models)

# Arbitrary number of arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
# *toppings makes an empty tuple called toppings and packs all the values in to the tuple

# Arbitrary list needs to come last, after positional and keyword arguments

# If you have an arbitrary number of different types you can use the following
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics',
                                age=25)

print(user_profile)
 
# Functions can be stored in a separate module and then imported
# import pizza looks for the file pizza.py and copies in all the functions from it
# now just use pizza.function_name() syntax to call functions from it
 
# You can also import just some functions
# from module_name import function_name[,function_name2,function_name3]
# with this syntax we don't need "." notation, just use the function name to call it

# Give a function an alias with as
# from pizza import make_pizza as mp
# make_pizza function now called as mp() no . notation needed

# You can also give a module an alias
# import pizza as p
# p.make_pizza()

# You can also import each function directly
# from pizza import *
# But this could have lots of name collisions (no . needed) so be careful
# Python overwrites when a new function name comes along
       
