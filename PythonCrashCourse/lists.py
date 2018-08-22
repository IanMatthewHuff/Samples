bikes = ['trek', 'giant', 'huffy']
print(bikes)
# python prints the data structure of the list

# access via index
print(bikes[1])

# can use string functions on access items
print(bikes[2].title())

# access items from the end starting with -1
print(bikes[-1].title())
# prints same as the previous one. Can use -2 for second from end and so on

message = "My first bike was a " + bikes[0].title()
print(message)

bikes[1] = 'lime'
print(bikes)

bikes.append('haro')
bikes.insert(0, 'cannondale')

print(bikes)

# del statement to remove from list
del bikes[1]

# pop removes the last element, but also returns it
popped_bike = bikes.pop()
print(bikes)
print(popped_bike)
# pop can also take an index to pop element at that position

# you can remove to remove by value, error if not present
bikes.remove('lime')
print(bikes)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# alphabetical order
cars.sort(reverse=True)
# reverse alpha order
print(cars)

# sort() is a perm change, sorted() doesn't actually change the list
print(sorted(cars))

# reverse the list
cars.reverse()
print(cars)

list_length = len(cars)
print("length of the cars list is: " + str(list_length))

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick " + magician.title() + ".\n")

print("Thanks everyone, that was a great show \n")

# range() function used to create a range of numbers
for value in range(1,5):
    print(value)
# THIS ONLY PRINTS  1 - 4
# Counting stops right as the second number is reached

# use list to create a list from a range
numbers = list(range(1,6))
print(numbers)

# range can skip numbers as well
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# start at 2, stop at 11, count by 2s

# now try to create first 10 squares
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions simplify list creation and generation
new_squares = [value**2 for value in range(1,11)]
print(new_squares)
# define the expression for the values you want in the list (value ** 2)
# then the for loop of elements to feed into the expression (value in range(1,11))

# slices to access sublists
players = ["tom", "joe", "lisa", "barry", "eli"]
print(players[0:3])
# prints first three players as it stops (before taking) index 3

print(players[1:4])
# prints joe -> barry

# if you omit the first index it starts at the start
print(players[:4])

# omit second number to slice to end
print(players[2:])

# can also use negative indexing
print(players[-2:])

print("First three players on my team: \n")
for player in players[:3]:
    print(player.title())

# copy a list with [:]
new_players = players[:]
# fully new list, can add different items to each
# if you just use new_players = players you get variable to point at the same list

# tuples are immutable lists
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# you would get a type error if you do. dimensions[1] = 10

for dimension in dimensions:
    print(dimension)

# you can overwrite the var with a new tuple
dimensions = (400, 100)

