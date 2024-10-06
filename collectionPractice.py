# do not name a file 'collections' it causes errors
# collection = single "variable" used to store multiple variables
# List = [] ordered and changeable, duplicates allowed
# Set = {} unordered and immutable, Add/Remove allowed, no duplicates
# Tuple = () ordered and unchangeable, duplicates allowed, faster

fruits = ["apple", "orange", "banana", "coconut"]

#print(dir(fruits)) # dir stands for directory, shows all variables and functions of Lists
#print(help(fruits)) # help page for Lists

print(len(fruits)) # returns length of List
print("apple" in fruits) # 'in' operator allows for quick checking if an item is in a List or not, returns boolean

# print(fruits) # prints List as it is declared
#print(fruits[0]) # works like an array
#print(fruits[::-1]) # index operators also work here, -1 step prints it backwards

#for fruit in fruits:
#    print(fruit)