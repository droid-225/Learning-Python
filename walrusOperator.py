# walrus operator :=
# also called the assignment expression
# assigns values to variables as part of a larger expression
# works for python 3.8+

# happy = True
# print(happy)

#print(happy := True) # print(happy = True) does not work

foods = list()

#while True:
#    food = input("What food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)

while food := input("What food do you like?: ") != "quit":
    foods.append(food)