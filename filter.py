# filter() : creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)

friends = [("Ross", 20),
           ("Joey", 16),
           ("Monica", 18),
           ("Rachel", 19),
           ("Phoebe", 17),
           ("Chandler", 21)]

age = lambda data: data[1] >= 18

drinkable = list(filter(age, friends))

for i in drinkable:
    print(i)