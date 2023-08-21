import turtle
import random

def square():
    for i in range(4):
        small.forward(front)
        small.right(90)

def circle():
    small.circle(front/2)

def triangle():
    for i in range(4):
        small.forward(front)
        small.right(120)

def polygon():
    angle = 360 / sides
    for _ in range(sides):
        small.forward(front)
        small.right(angle)

small = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
small.pensize(random.randint(2, 4))
small.speed(15)

front = random.randint(50, 100)
circleSize = random.randint(1, 10)

colours = [("cyan2", "cyan4"), ("darkgoldenrod1", "darkgoldenrod"), ("darkorchid2", "darkorchid4"), ("chocolate1", "chocolate3"), ("brown4", "brown3"), ("darkolivegreen2", "darkolivegreen4")]
theact = random.choice(colours)

times = random.randint(25, 100)
print(f"times: {times}")

angle = random.randint(0, 359)
print(f"angle: {angle}")

notig = [square, circle, triangle, polygon]

Obama = random.choice(notig)
print(Obama)

if random.randint(0, 3) == 1:
    for i in range(times):
        small.color(random.choice(colours)[i % 2])
        small.right(angle)
else:
    sides = random.randint(3, 10)
    for i in range(times):
        small.color(theact[i % 2])
        Obama()
        small.right(angle)

window.exitonclick()