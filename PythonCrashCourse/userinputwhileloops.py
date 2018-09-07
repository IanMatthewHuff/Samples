# input function waits for the user to enter text
message = input("Tell me something and I'll repeat it back: ")
print(message)

prompt = "Tell us your name."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

# int() gets numeric input
age = input("How old are you? ")
age = int(age)
age >= 18

number = input("Enter number, even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number" + str(number) + " is even.")
else:
    print("\nThe number" + str(number) + " is odd.")

# in python 2 you need to use raw_input instead of input

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to" + city.title() + "!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users are confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# while loops for all the instances of that value in the list
pets = ['dog','cat','dog','fish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


