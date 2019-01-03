import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj2:
    numbersLoad = json.load(f_obj2)

print(numbersLoad)    

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj3:
    json.dump(username, f_obj3)
    print("We'll remember you when you come back, " + username + "!")

with open(filename) as f_obj4:
    username = json.load(f_obj4)
    print("Welcome back, " + username + "!")

