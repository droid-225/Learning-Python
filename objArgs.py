# objects as arguments
class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color

car1 = Car()
car2 = Car()
car3 = Car()
bike1 = Motorcycle()

change_color(car1, "blue")
change_color(car2, "red")
change_color(car3, "green")
change_color(bike1, "amber")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)
