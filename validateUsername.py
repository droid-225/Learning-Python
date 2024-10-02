# rules:
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

username = input("Enter a Username: ")

if len(username) > 12:
    print("The username cannot be more than 12 characters")
elif username.find(" ") != -1:
    print("The username cannot contain spaces")
elif not username.isalpha():
    print("The username can only contain alphabetical values")
else:
    print(f"Welcome {username}!")
