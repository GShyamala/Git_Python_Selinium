#Single Inheritance
# class vehicle():
#     def speed(self):
#         print("Average speed is 45")
#     def wheels(self):
#         print("Can contain 2wheelas or 4 wheels")
#
# class car(vehicle):
#     def speed(self):
#         print("car speed is 60")
#     def color(self):
#         print("color is Red")
#
# c=car()
# c.speed()
# c.wheels()
# c.color()
#Multi level Inheritance
# class vehicle():
#     def speed(self):
#         print("Average speed is 45")
#     def wheels(self):
#         print("Can contain 2wheelas or 4 wheels")
#
# class car(vehicle):
#     def speed(self):
#         print("car speed is 60")
#     def color(self):
#         print("color is Red")
#
# class maruti(car):
#     def gear(self):
#         print("Automatic gear")
#     def light(self):
#         print("Lights are bright")
#
# m=maruti()
# m.gear()
# m.light()
# m.speed()
# m.wheels()
# m.color()

#Multiple Inheritance
# class vehicle():
#     def speed(self):
#         print("Average speed is 45")
#
#     def wheels(self):
#         print("Can contain 2wheelas or 4 wheels")
#
# class car():
#     def speed(self):
#         print("car speed is 60")
#
#     def color(self):
#         print("color is Red")
#
# class maruti(vehicle,car):
#     def gear(self):
#         print("Automatic gear")
#
#     def light(self):
#         print("Lights are bright")
# m = maruti()
# m.gear()
# m.light()
# m.speed()
# m.wheels()
# m.color()

#Hierarchical Inheritance
# class vehicle():
#     def speed(self):
#         print("Average speed is 45")
#     def wheels(self):
#         print("Can contain 2wheelas or 4 wheels")
#
# class car(vehicle):
#     def speed(self):
#         print("car speed is 60")
#     def color(self):
#         print("color is Red")
# c=car()
# c.speed()
# c.color()
# c.wheels()
# class maruti(vehicle):
#     def gear(self):
#         print("Automatic gear")
#     def light(self):
#         print("Lights are bright")
# m = maruti()
# m.gear()
# m.light()
# m.speed()
# m.wheels()
#Hybrid Inheritance
class vehicle():
    def speed(self):
        print("Average speed is 45")
    def wheels(self):
        print("Can contain 2wheelas or 4 wheels")
class car(vehicle):
    def speed(self):
        print("car speed is 60")
    def color(self):
        print("color is Red")
class maruti(vehicle):
    def gear(self):
        print("Automatic gear")
    def light(self):
        print("Lights are bright")
class marutiCar_features(maruti,car):
    def petrol(self):
        print("Its a petrol car")
    def type(self):
        print("Its a SUV type car")
m=marutiCar_features()
m.petrol()
m.type()
m.gear()
m.light()
m.speed()
m.wheels()
m.color()