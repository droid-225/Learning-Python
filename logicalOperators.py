money = 10
party_time = True

# or
#if money > 0 or party_time:
#    print("It's party time!")
#else:
#    print("It's not party time :(")

# and
#if money > 0 and party_time:
#    print("It's mega party time :D")
#elif money <= 0 and party_time:
#    print("It's normal party time!")
#else:
#    print("Can't party :(")

# not
#if money and not party_time:
#    print("I got money, but no party :(")
#elif money and party_time:
#    print("It's party time!")

# conditional expression (ternary operator)
# Syntax: X if condition else Y
#print("I got money" if money > 0 else "I got no money")
#print("Party Time" if party_time else "Not Party Time")
a = 6
b = 5
max = a if a > b else b
min = a if a < b else b
print(f"Max = {max}")
print(f"Min = {min}")