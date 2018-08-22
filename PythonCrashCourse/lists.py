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


