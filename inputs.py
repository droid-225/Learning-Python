name = input("What is your name? ") #function automatically prompts user to enter a value
# input function does basically nothing unless it is assigned to a variable
#age = input("How old are you? ")
# when we accept user input, that input is stored as a string
age = int(input("How old are you? "))

#age = int(age)
age = age + 1

print(f"\nHello {name}")
print("Happy Birthday!")
print(f"You are {age} years old")