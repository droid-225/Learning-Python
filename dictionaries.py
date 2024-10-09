# dictionary = a collection of {key:value} pairs
#             ordered and changeable, no duplicates

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

#print(dir(capitals)) # prints attributes and functions of dictionary
#print(help(capitals)) # prints help screen for dictionary

#print(capitals.get("USA")) # returns value related to given key
# if key does not have a value, or does not exit in the dictionary, it prints 'none'

#if capitals.get("Russia"): # get method can be used to check if a key has a value
#    print("That capital exists")
#else:
#    print("That capital exists")

# update method can be used to both add new key value pairs and change existing ones
#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})

#capitals.pop("China") # removes key value pair correlated to the given key
#capitals.popitem() # removes the last key value pair in the dictionary

#keys = capitals.keys() # keys method returns all keys in the dictionary, without their values

# the keys can be printed as such
#for key in capitals.keys():
#    print(key)

# they can also be printed this way, here they are treated as a List like object
#print(keys)

#values = capitals.values() # values method is like the keys method, but with values
#print(values) # prints values as a List like object
#for value in capitals.values(): # prints all values
#    print(value)

#items = capitals.items() # items method returns a 2D List like object with each row being a key value pair
#print(items)
for key, value in capitals.items(): # prints the keys and values corresponding to them
    print(f"{key}: {value}")

#print(capitals)

