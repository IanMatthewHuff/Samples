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

