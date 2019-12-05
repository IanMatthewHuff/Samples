# in Python 3 strings are unicode characters
# Character to actual bytes depends on encoding used
s41 = 'café'
len(s41)
b41 = s41.encode('utf8')
b41
len(b41)
b41.decode('utf8')

# bytes and bytearray for actual bytes
# each item is int from 0 to 255

# for display if printable ASCII use that, \x for escape chars
# and \x00 for other byte values
cafe_bytes = bytes('café', encoding='utf_8')
cafe_bytes
len(cafe_bytes)

# initialize bytes from the raw array data
import array
# h = short (16 bits)
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
octets

# struct module provides functions to pack bytes into tuples of different types
# and the opposite conversion
# memoryview provides shared memory access to slices of data without copying bytes
# doing a new bytes will always copy the bytes

# Python bundles more than 100 codecs for text -> byte in it

# Convert to str as quick as possible
# Do all business logic
# Convert back to bytes as late as you can

# for local specific string comparisons use locale import settings
# pyUCA is a better library to simply support this

