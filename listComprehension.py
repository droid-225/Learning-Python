# List Comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      Format: [expression for value in iterable if condition]

#doubles = []
#for x in range(1, 11):
#    doubles.append(x * 2)

# We can compact the above code as such:
#doubles = [x * 2 for x in range(1, 11)]

#print(doubles)

#fruits = ["apple", "orange", "banana", "coconut"]
#fruit_chars = [fruit[0] for fruit in fruits]

#print(fruit_chars)

# Using conditions:
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]

print(positive_nums)
print(negative_nums)