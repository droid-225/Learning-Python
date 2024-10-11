import random

#print(help(random)) # help page for the 'random' module

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#number = random.randint(1, 6) # 'randint' function returns a random number in the given range
# the range is inclusive on both sides, e.g. in this case it prints numbers in [1, 6]

#number = random.randint(low, high) # range can contain variables as long as they contain numbers

#number = random.random() # generates a random floating point value between 0 and 1

#option = random.choice(options) # chooses a random element from given tuple

random.shuffle(cards) # randomly rearranges elements in given List

print(cards)