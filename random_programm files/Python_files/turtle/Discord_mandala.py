import turtle
import random
import time


def square():
    for i in range(5):
        small.forward(front)
        small.right(90)


def circle():
    small.circle(front/2)


def triangle():
    for i in range(3):
        small.right(120)
        small.forward(front)


def polygon():
    for i in range(100):
        small.forward(front)
        small.right(front)

small = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
small.pensize(random.randint(2, 4))


small.speed(15)
front = random.randint(50, 100)
circleSize = random.randint(1, 10)


colour = (("cyan2", "cyan4"),("darkgoldenrod1", "darkgoldenrod"),("darkorchid2", "darkorchid4"),("chocolate1","chocolate3"),("brown4", "brown3"),("darkolivegreen2","darkolivegreen4"))
theact= colour[random.randint(0,4)]


times = random.randint(25, 100)  # int(input("How many loops?"))
print(f"times: {times}")

angle = random.randint(0, 359)
print(f"angle: {angle}")

notig= (square(),circle(),triangle(),polygon())

Obama = notig[random.randint(0,3)]
print(Obama)

# if random.randint(0,3) == 1:
#     for i in range(times):
#         small.color(colour[random.randint(0, 5)][i % 2])
#         small.right(angle)
#
# else:
#     for i in range(times):
#         small.color(theact[i % 2])
#         square()
#         small.right(angle)


for i in range(times):
        small.color(theact[i % 2])
        square()
        small.right(angle)



window.exitonclick()
