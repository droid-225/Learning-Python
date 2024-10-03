nameEntered = False
name = input("Enter your name: ")

while name == "":
    print("You did not enter a name!")
    name = input("\nEnter your name: ")

print(f"Hello {name}")

# while True:
#   condition:
#       break
# this also works if you want to break only when a condition is met or not met