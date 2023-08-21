import turtle
import math

ich=turtle.Turtle()
window=turtle.Screen()


ich.pensize(3)
ich.speed(10)


# ich.circle(100)

n= 50

for i in range(10):
    ich.forward(n*2)
    ich.right(n)
#
#
#
#

colour = (("brown4", "brown3"),("cyan3", "cyan4"),("darkgoldenrod1", "darkgoldenrod2"),("darkorchid3", "darkorchid4"),("chocolate1","chocolate3"))

print(colour[0][1])

d=colour[2]
print(d)

print(d[0],d[1])






window.exitonclick()