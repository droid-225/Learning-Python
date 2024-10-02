# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

cardNumber = "1234-5678-9012-3456"

# when having only one field filled in without any colons, it assumes you are inputting the starting position
#print(cardNumber[4])

#print(cardNumber[-1]) # negative numbers make it go backwards from last value in the string (-1 is the last value)

#print(cardNumber[0:4]) # returns value at index 0 to 3 (end number is exclusive i.e. [0,4))
#print(cardNumber[:4]) # this also works if start value is 0
#print(cardNumber[4:]) # this works if end value is the last value in the string

#print(cardNumber[::2]) # returns every 2 digits in the whole string (starting from 0)

# returns last four values of string
#lastDigits = cardNumber[-4:]
#print(f"XXXX-XXXX-XXXX-{lastDigits}")

# print string in reverse
print(cardNumber[::-1]) # -1 is in the step field so it goes backwards
