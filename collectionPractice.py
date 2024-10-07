# do not name a file 'collections' it causes errors
# collection = single "variable" used to store multiple variables
# List = [] ordered and changeable, duplicates allowed
# Set = {} unordered and immutable, Add/Remove allowed, no duplicates, indexing not allowed
# Tuple = () ordered and unchangeable, duplicates allowed, faster

# List
#fruits = ["apple", "orange", "banana", "coconut"]

#print(dir(fruits)) # dir stands for directory, shows all variables and functions of Lists
#print(help(fruits)) # help page for Lists

#print(len(fruits)) # returns length of List
#print("apple" in fruits) # 'in' operator allows for quick checking if an item is in a List or not, returns boolean

#fruits[0] = "pineapple" # changing values works like an array
#fruits.append("pineapple") # adds value to end of List
#fruits.remove("apple") # removes given value
#fruits.insert(1, "pineapple") # inserts given value and pushes other values forward
#fruits.sort() # sorts values, in this case it is sorted alphabetically
#fruits.reverse() # reverses order of List
#fruits.clear() # clears List
#print(fruits.index("apple")) # index method returns index value of given value
# throws error when value is not found

#fruits.append("banana")
#print(fruits.count("banana")) # returns number of times the given value occurs in the List

#print(fruits) # prints List as it is declared
#print(fruits[0]) # works like an array
#print(fruits[::-1]) # index operators also work here, -1 step prints it backwards

#for fruit in fruits:
#    print(fruit)

# Set
#fruits = {"apple", "orange", "banana", "coconut"}

#print(dir(fruits)) # prints all values and methods of Set
#print(help(fruits)) # prints help page for Set

#print(len(fruits)) # returns length of the set
#print("pineapple" in fruits) # works same as in List

#fruits.add("pineapple") # adds the given value to a random spot in the set
#fruits.remove("apple") # removes given value
#fruits.pop() # removes first element, also random
#fruits.clear() # clears the set

#fruits.add("apple") # although 'apple' occurs twice, it will only be printed once as no duplicates can exist in the set

#print(fruits) # since sets are unordered, the set will be printed in a different order every time

# Tuple
fruits = ("apple", "orange", "banana", "coconut", "coconut")

#print(dir(fruits)) # prints all values and methods of Tuple
#print(help(fruits)) # prints help page for Tuple

#print(len(fruits)) # returns length of the tuple
#print("pineapple" in fruits) # works same as in List

#print(fruits.index("apple")) # returns index of given value
#print(fruits.count("coconut")) # returns number of times the given value occurs

# for loop can be used to iterate through the tuple

print(fruits)
