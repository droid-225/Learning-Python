# list comprehensions : a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       formula: list = [expression for item in iterable if conditional] (conditional is optional)
#                       if expression requires if else,
#                       formula: list = [expression (if/else) for item in iterable]

#squares = []
#for i in range(1, 11):
#    squares.append(i * i)
#print(squares)

#squares = [i * i for i in range(1, 11)]
#print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
#passed = list(filter(lambda x: x >= 60, students))
#passed = [i for i in students if i >= 60]
passed = [i if i >= 60 else "FAILED" for i in students]
print(passed)