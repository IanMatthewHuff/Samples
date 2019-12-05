# Dicts are use to build a huge amount of base python funtionality
# so they need to be high perfomance in python

# collections.abc module provides abcs to formalize the interface of dict and types
# MutableMapping imp by Mapping imp by Container, Iterable, Sized

# Implementations of specialized mappings often extend dict or collections.UserDict instead of ABCs
# Main value of ABCs of documenting and formalizing minimal interfaces for mappings
import collections.abc
my_dict = {}
isinstance(my_dict, collections.abc.Mapping)

# all keys must be hashable
# Has hash value __hash__() that never changes in its lifetime
# equal objects must have equal hashes
# atomic mutable types are all hashable
# so a frozenset is hashable, but a list is not
tt = (1, 2, (30, 40))
hash(tt)
tl = (1, 2, [30, 40])
hash(tl) # TypeError: unhashable type: 'list'
tf = (1, 2, frozenset([30, 40]))
hash(tf)

# Different ways to build a dict
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e

# Dict comp
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States')
]

country_code = {country: code for code, country in DIAL_CODES}
country_code
# dict can use a list of pairs

# for a dict if you provide a __missing__ method this will be called
# with a missing key as opposed to raising KeyError

# can get a default or test with 'in'
dz = {1:1, 2:2, 3:3}
print(dz[0]) #KeyError
print(dz.get(0, 'default_value'))
print(0 in dz)

# For your own class easier to start with UserDict and not dict

# Here is example of a class to take strings or values for keys
class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# Set and frozenset
# Collections of unique items
sl = ['spam', 'eggs', 'spam', 'eggs']
set(sl) # {'eggs', 'spam'}
list(set(sl)) # ['eggs', 'spam'] 

# can use set operations like | = union, & = intersection, - is difference

# instead of this
found = 0
for n in needles:
    if n in haystack:
        found += 1

# do this
found = len(needles & haystack)

# set literals look like math notation {1}, {1, 2}, ect... but for an
# empty set we must use set() as {} is an empty dict
# frozenset must use frozenset constructor

# there are set comps just like dict and list comps
from unicodedata import name
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}

# in P3 .keys .items and .values from a dict return views
# These are more like sets versus lists and reflect changes in the dict
# right away

