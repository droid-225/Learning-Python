# *args    = allows you to pass multiple non-key arguments, stores values in a tuple
# **kwargs = allows you to pass multiple keyword arguments, stores values in a dictionary
#            * is the unpacking operator

# *args
#def add(*args): # you can name the parameter anything besides args, but it must have a * in front
#    total = 0
    #print(type(args))
#    for arg in args:
#        total += arg
#    return total

#add(1, 2, 3)
#print(add(1, 2, 3))

# **kwargs
#def print_address(**kwargs):
    #print(type(kwargs))
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")

#print_address(street="Bubble Lane",
#              apt="1001",
#              city="Chicago",
#              state="Illinois",
#              zip="12345")

def shipping_label(*args, **kwargs): # args must come before kwargs
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Baker St.",
               apt="101",
               city="Detorit",
               state="MI",
               zip="23453")