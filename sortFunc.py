# sort() method : used with lists
# sorted() function : used with iterables

#students = ["Squid", "Sponge", "Pat", "Sandy"]
#studTuple = ("Squid", "Sponge", "Pat", "Sandy")

#students.sort() # only works with lists
#sortedStudents = sorted(students, reverse=True) # returns sorted list

#for i in sortedStudents:
#    print(i)

students = [("Squidward", "D", 60),
            ("Sandy", "A", 33),
            ("Spoingbob", "B", 34),
            ("Patrick", "F", 35)]

studentTuple = (("Squidward", "D", 60),
            ("Sandy", "A", 33),
            ("Spoingbob", "B", 34),
            ("Patrick", "F", 35))

grade = lambda grades: grades[1]
age = lambda ages: ages[2]
students.sort(key=age)

sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)