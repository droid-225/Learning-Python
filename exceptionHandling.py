# exception = events detected during execution that interrupt the flow a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))

    result = numerator / denominator
except ZeroDivisionError as e:
    print("You can't divide by zero!")
    print(e)
except ValueError as e:
    print("Please only enter numbers!")
    print(e)
except Exception as e: # better to write specific exceptions before the general Exception
    print("Something went wrong!")
    print(e)
else: # only occurs if no exception occurs
    print(result)
finally: # always executes, and always at the end
    print("We did a thing!")