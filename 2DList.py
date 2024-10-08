fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats] # 2D List, or a List of Lists

# Can also be written as:
# groceries = [["apple", "orange", "banana", "coconut"]
#              ["celery", "carrots", "potatoes"]
#              ["chicken", "fish", "turkey"]]

#print(groceries[0]) # prints entire row specified
#print(groceries[2][2]) # works like 2D array, [row][column]

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()