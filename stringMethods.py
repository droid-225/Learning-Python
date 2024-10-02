name = input("Enter your name: ")

stringLength = len(name) # returns length of string including spaces

find = name.find(" ") # returns the index of the first occurrence of the string given (starting with 0)
find = name.rfind("s") # returns the index of the last occurrence of the string given (starting with 0)
# both find functions are case-sensitive
# they return -1 if no results are found

#name = name.capitalize() # returns string after capitalizing the first letter

#name = name.upper() # makes all characters in string into uppercase
#name = name.lower() # makes all characters in string into lowercase

digitCheck = name.isdigit() # returns True only if string only contains digits, otherwise False
alphaCheck = name.isalpha() # returns True only if string only contains alphabetical characters, otherwise False
# spaces also count as non-alphabetical characters

count = name.count("r") # returns number of specified characters are in the string

newName = name.replace("s", "w") # returns string after replacing old character with new character

print(newName)

#print(help(str)) # displays all str methods