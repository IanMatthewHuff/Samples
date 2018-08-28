cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# True or False python truth values
# Python is case sensitive for equality checks

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Most basic math stuff available <= > >= <

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_0 >= 21 or age_1 >= 21

requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title() + " , you can post.")

age = 17
if age >= 18:
    print("you are old enough to vote.")
    print("Have you registered to vote?")
else:
    print("sorry, you are too young to vote.")

age = 12
if age < 4:
    print("Admission: $0.")
elif age < 18:
    print("Admission: $5.")
else:
    print("Admission: $10.")

empty_list = []

if empty_list:
    #do stuff
else:
    print("This list is empty")
# IF list is empty the name of the list evaluates to False


