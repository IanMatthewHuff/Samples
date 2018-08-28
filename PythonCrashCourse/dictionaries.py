alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

# Colleciton of key value pairs
# Any python object can be a value in the dictionary
# Braces with sets of key value pairs to initialize
alien_0['xpos'] = 0
alien_0['ypos'] = 25
print(alien_0)

alien_z = {} # can define empty and then add
alien_z = {'color':'green'}
alien_z['color'] = 'yellow'

# you can delete with the del statement
alien_z['points'] = 5
del alien_z['points']

# can group with spaceing
favorite_lang = {
    'jen':'python',
    'sarah':'c',
    'phil':'ruby',
}

print("Sarah's favorite language is " +
    favorite_lang['sarah'].title() +
    ".")

# you can loop through a dictionary as well
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
# note we picked the key and value names
# they could be anything, just order of key and then value
# also not not in order as dictionaries are not ordered

for name in favorite_lang.keys():
    print(name.title())

if 'erin' not in favorite_lang.keys():
    print("Erin please take our poll!")

# use sorted if you actually want sorted order
for name in sorted(favorite_lang.keys()):
    print(name.title(), ", thank you for taking our poll!")

print("The following languages have been mentioned:")
for language in favorite_lang.values():
    print(language.title())

# use a set to not have any repeats
print("The following unique languages")
for language in set(favorite_lang.values()):
    print(language.title())

# dictionaries and lists can nest inside each other
alien_a = {'color':'green', 'points':5}
alien_b = {'color':'yellow', 'points':10}
alien_c = {'color':'red', 'points':15}

aliens = [alien_a, alien_b, alien_c]

for alien in aliens:
    print(alien)

aliens2 = []
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens2.append(new_alien)

for alien in aliens2[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

# also a list can go in a dictionary
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# dictionary in dictionary
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


