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