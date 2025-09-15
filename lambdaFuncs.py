# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
# syntax: lambda parameters: expression

#def double(x):
#    return x * 2

double = lambda x: x * 2
multiply = lambda x, y: x * y
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(double(53))
print(multiply(4, 5))
print(full_name("Rishit", "Shah"))
print(age_check(22))