# can be used to iterate over a range string, sequence, etx.

#for x in reversed(range(1, 11, 2)): # second number is exclusive, third number is step counter
    # reversed function used to count backwards
#    print(x)

#cardNumber = "1234511234"

#for x in cardNumber:
#    print(x)

for x in range(1, 21):
    if x == 13:
        continue # continue keyword used to skip and iteration
    elif x == 15:
        break # break works as usual
    else:
        print(x)
