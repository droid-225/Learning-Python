# format specifiers = {value:flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value, does not affect negative numbers
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator (e.g. like in 1,000)
# These can be combined

price1 = 3.35234
price2 = -5.34634
price3 = 6.32423

print(f"Price1 is ${price1:.2f}")   # rounds number to two decimal spaces
print(f"Price2 is ${price2:10}")    # left aligns number and adds padding to reach specified spaces
print(f"Price3 is ${price3:010}")   # same as before but adds 0's instead of spaces as padding
