age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
elif age < 0:
    print("You Lied!")
else:
    print("You are not 18 or older.")