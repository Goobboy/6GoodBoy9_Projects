import turtle
import random


def polygon():
    for i in range(100):
        small.forward(front)
        small.right(angle)



small = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")

small.pensize(random.randint(2, 4))
small.speed(100)
front = random.randint(50, 150)
print(f"\nLength/(radius/2): {front}")
circleSize = random.randint(50, 100)

tree= random.randint(3,5)


colour = (("cyan2", "cyan4"),("darkgoldenrod1", "darkgoldenrod"),("darkorchid2", "darkorchid4"),("chocolate1","chocolate3"),("brown4", "brown3"),("darkolivegreen2","darkolivegreen4"))
theact= colour[random.randint(0,1)]


times = random.randint(50, 80)  # int(input("How many loops?"))
print(f"times: {times}")

angle = random.randint(0, 359)
saver= random.randint(0,3)
small.color("red")


# if random.randint(0, 3) == 1:
#     print(f"angle: {angle}")
#     print("polygon1")
#     for i in range(times):
#         small.color(colour[random.randint(0, 5)][i % 2])
#         polygon()
#         small.right(angle)
#
# else:
#     print("polygon2")
#     print(f"angle: {angle}")
#     for i in range(times):
#         small.color(theact[i % 2])
#         polygon()
#         small.right(angle)



n= 50

for i in range(10):
    small.forward(n*2)
    small.right(n)

window.exitonclick()
