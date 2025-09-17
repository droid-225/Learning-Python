# zip(*iterables) : aggregates elements from two or more iterables.
#                   creates a zip object with paired elements stored in tuples for each element.

usernames = ["Dude", "Bro", "Mr"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

#users = dict(zip(usernames, passwords)) # converts zip to list

#print(type(users))

#for key, value in users.items():
#    print(key + ": " + value)

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)