# Higher Order Functions: A function that either:
#                         1. accepts a function as an argument
#                           or
#                         2. returns a function
# python treats functions as objects

# function that accepts a function as an argument:
#def loud(text):
#    return text.upper()

#def quiet(text):
#    return text.lower()

#def hello(func):
#    text = func("Hello")
#    print(text)

#hello(quiet)

# a function that returns a function:
def divisor(x):
    def dividend(y):
        return y / x

    return dividend

divide = divisor(2)
print(divide(4))