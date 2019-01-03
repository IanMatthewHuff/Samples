with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Open function to open a file and store as file_object
# With allows python to close the file automatically when no longer needed

# Read reads an extra empty line at the end. You can use rstrip() to remove this

filename = 'pi_digits.txt'

with open(filename) as file_object2:
    for line in file_object2:
        print(line.rstrip())

pi_string = ''
with open(filename) as file_object3:
    lines = file_object3.readlines()

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

filename = 'programming.txt'
with open(filename, 'w') as file_object4:
    file_object4.write("I Love Programming.\n")
    file_object4.write("I Love Creating New Games.\n")

# -w is write mode, r = read, w = write, a = append, read / write = r+ read-only is default
# if file exists w will erase the existing file

with open(filename, 'a') as file_object5:
    file_object5.write("I also love working with large datasets.\n")



