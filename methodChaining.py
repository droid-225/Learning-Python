class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off() # methods are executed in sequential order
# this requires the called methods to have a return value, which is not default
# if returning nothing, at least return self
# this format is recommended for longer method chains