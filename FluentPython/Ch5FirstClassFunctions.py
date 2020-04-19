# Functions in python can be treated like other variables
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)


factorial(42)
factorial.__doc__
type(factorial)

# Can assign function to variable
fact = factorial
fact
fact(5)
map(factorial, range(11))
list(map(fact, range(11)))

# Higher order functions take a function as arg or return a function
# map is a built in example of this or sorted
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=len)  # Sort by length

# example of sorting in reverse order
def reverse(word):
    return word[::-1]


reverse('testing')
sorted(fruits, key=reverse)

# Python still provides map, filter and reduce, but there are better options

# List comps can stand in better for map and filter
list(map(fact, range(6)))
[fact(n) for n in range(6)]
list(map(factorial, filter(lambda n: n % 2, range(6))))
[factorial(n) for n in range(6) if n % 2]

# reduce is still avail in functools, but sum operator does it better
from functools import reduce
from operator import add
reduce(add, range(100))
sum(range(100))

# all and any also useful for reducing (all = everything is true, any = something true)

# Anon functions created with lambda keyword
# In python, body of lambda must be pure expression, no assignments or other python statements
sorted(fruits, key=lambda word: word[::-1])

# you can use the call operator (ie ()) on anything that is callable()
[callable(obj) for obj in (abs, str, 13)]  # True, True, False

# Implement __call__ to make something callable
# BingoCage to pick from shuffled list
import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
bingo.pick()
bingo()
callable(bingo)

# Function introspection functions have many attributes past __doc__
# dir function can show other attributes on our functions

def tag(name, *content, cls=None, **attrs):
    ''' Generate one or more HTML tags'''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                        for attr, value
                        in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                            (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

tag('br')
print(tag('p', 'hello', 'world'))
tag('p', 'hello', id=33)

# Single positional argument makes empty HTML tag with that name
# any number of args after the first are captures by *content as tuple
# keyword arguments not specified in def of tag captured by **attrs as dict
# cls can only be passed by keyword

# you can use ** to explode a dict into parameters
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 
            'src': 'sunset.jpg', 'cls': 'framed'}
tag(**my_tag)
# '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'

# keyword only params must come after * params, if you don't want * params just empty *
def f(a, *, b):
    return a, b

f(1, b=2)

# we can introspect what the paramters of a function are
def clip(text, max_len=80):
    '''Return text clipped at the last space'''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

clip.__defaults__
clip.__code__
clip.__code__.co_varnames
clip.__code__.co_argcount

# this data is very split up, so the inspect module is usually a better option
from inspect import signature
sig = signature(clip)
sig
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

# inspect.Signature object has a bind method to validate parameters
# before actually invoking a function TypeError if bind fails

# you can annotate in Python 3
# def clip(text:str, max_len:'int > 0'=80) -> str:
# stored in .__annotations__ of the function
# these are not processed at all, just stored in __annotations__ you have to do something with them

# Packages for Functional programming
from functools import reduce

def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

from operator import mul
def fact2(n):
    return reduce(mul, range(1, n+1))

# Other helper functions to avoid writing small lambdas like itemgetter for []
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.68, 139.69)),
    ('Mexico City', 'MX', 20.14, (19.43, -99.13))
]

from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

# Sorting by [1] in the items
# multiple index to itemgetter returns as tuple
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

# attrgetter gets attributes by name, can navigate levels with . operator

# Methodcaller can call a method with given params
# could use to freeze some params
from operator import methodcaller
s = 'The time has come'
hiphenate = methodcaller('replace', ' ', '-')
hiphenate(s)

# functools partial allows for partial application of a function
from operator import mul
from functools import partial
triple = partial(mul, 3)
triple(7)

# using our tag class from ealier
picture = partial(tag, 'img', cls='pic-frame')
picture(src='wumpus.jpeg')

