from collections import namedtuple
import bisect
import random

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# Note: tshirts order is same as outer colors inner size nested fors

# listcomps are just for lists, genexp for others
# genexp does one item at a time to feed so doesn't have to create
# a new list like making a listcomp to feed

for tshirt2 in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt2)

# tuples as immutable lists and records with no field names

# can unpack to variables
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

# % can also unpack into format variables
print('%s %s %s %s %s' % ('Tokyo', 2003, 32450, 0.66, 8014))

# You can unpack any iterable if you match the number of variables desired
# of if you use * to capture excess items

divmod(20, 8)
t = (20, 8)
divmod(*t)
quotient, remainder = divmod(*t)

# * is used to grab excess args
a, b, *rest = range(5)
a, b, rest
# (0, 1, [2, 3, 4])
a, *body, c, d = range(5)
# (0, [1, 2], 3, 4)

# we can unpack nested tuples if expression matches structure
metro_areas = [
    ('Tokyo', 'JP', 26.933, (35.68, 139.69)),
    ('Sau Paulo', 'BR', 19.649, (-23.54, -46.63))
]

for name, cc, pop, (lat, longi) in metro_areas:
    if longi > 0:
        print(name)

# named tuple basically the same just with a name for debugging
City = namedtuple('City', 'name country population coords')
tokyo = City('Tokyo', 'JP', 36.933, (35.68, 139.69))
# and you can access now with . operator
tokyo.population

# Slicing never includes the second item
l = [1, 2, 3, 4, 5]
l[:2] # Indexes 0 and 1 first two items
l[2:] # Start at index 2 until the end 3, 4, 5

# slices can be stored
firstTwo = slice(0, 2)
l[firstTwo] # Same as l[0:2]

# You can assign to the left side with slice notation
newList = list(range(10))
newList[2:5] = [20, 30]
newList

del newList[5:7]
newList

# Using + and * with sequences (both create a new object)
# * for sequences concatinates multiple copies of the sequence
l1 = [1, 2, 3]
l1 * 5
5 * 'abcd'

# To build a list of lists use a list comp, so we don't get three copies of the same list
board = [['_'] * 3 for i in range(3)]
board

# This is wrong and returns three copies of the same list
wrong_board = [['_'] * 3] * 3
wrong_board

# += calls __iadd__ but falls back on __add__ if not available
# so if a += b we might or might not change the identity of a as
# most mutable sequences implement __iadd__ and change in place
# so list += adds elements in place, tuple add elements creates a new object
# python tutor can help to visualize stuff like this

# list.sort and sorted function
# list.sort sorts in place. It indicates this by returning None
# however sorted returns a new sorted list
# arguments are reverse for reverse sorting and key for a one argument function to apply like len
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
fruits
sorted(fruits, reverse=True)
sorted(fruits, key=len)
sorted(fruits, key=len, reverse=True)
fruits
fruits.sort()
fruits

# Manage ordered sequences with bisect
# bisect module provides bisect and insort
# bisect(haystack, needle) does a binary search for needle in heystack - which must be sorted
# locates location where needle can be inserted in order, insort does find and insert in that position
# hi and lo arguments to restrict how much of the sequence to search. 
# bisect = bisect_right ties go to the right, there is also a bisect_left


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]

# Inserting with insort
SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

# Arrays if the list is only numbers array is more efficent. It's as lean as a C++ array
from array import array
from random import random
floats = array('d', (random() for i in range(10**3)))

# reading a big list of floats from a file is way faster with array.fromFile as opposed to strings
# pickle is also a great way of serializing

# memorview class is a shared memory type to look at slices of arrays without copying bytes
# inspired by numpy. Memoryview is generalized numpy array structure in python
# memoryview.cast returns another memory view object sharing the same memory
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv)
memv[0]
memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4
numbers

import numpy
a = numpy.arange(12)
a
a.shape
a.shape = 3,4
a
a[2]
a[2, 1]
a[:, 1]
a.transpose()
# high level operations for loading and saving from files

# .append and .pop make lists usable as a queue or stack
# but insert and remove on the left end is slow is costly as the list must be shifted

# use deque for better perf here
from collections import deque
dq = deque(range(10), maxlen=10)
dq
dq.rotate(3)
dq.extend([11, 22, 33])
dq.appendleft(-1)

# Can consider python seqences mutable or immutable or also 
# flat or container sequences. Flat = fast / easy, but type limited
# container = flexible
