# assigning function to variables

def hello():
    print("Hello!")

#print(hello) # prints location of function in memory in hexadecimal
hi = hello # assigns hi the same memory address as hello, giving hello an alias
#print(hi)

#hello()
#hi()

say = print # assigns address of print function to say
say("Hello World!")