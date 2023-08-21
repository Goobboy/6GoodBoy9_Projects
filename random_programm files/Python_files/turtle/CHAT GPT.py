import turtle
import random
import time


def draw_square(small, front):
    for _ in range(4):
        small.forward(front)
        small.right(90)


def draw_circle(small, radius):
    small.circle(radius)


def draw_triangle(small, front):
    for _ in range(3):
        small.forward(front)
        small.right(120)


def draw_polygon(small, front, sides):
    angle = 360 / sides
    for _ in range(sides):
        small.forward(front)
        small.right(angle)


small = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")

for _ in range(10):
    small.pensize(random.randint(2, 4))
    small.speed("fastest")
    front = random.randint(50, 150)
    print(f"\nLength/(radius/2): {front}")
    circleSize = random.randint(50, 100)

    colour = (("cyan2", "cyan4"), ("darkgoldenrod1", "darkgoldenrod"), ("darkorchid2", "darkorchid4"),
              ("chocolate1", "chocolate3"), ("brown4", "brown3"), ("darkolivegreen2", "darkolivegreen4"))
    chosen_colors = colour[random.randint(0, 5)]

    times = random.randint(50, 80)
    print(f"times: {times}")

    shape_choice = random.randint(0, 3)

    if shape_choice == 0:
        print("square")
        for i in range(times):
            small.color(chosen_colors[i % 2])
            draw_square(small, front)
            small.right(random.randint(0, 359))

    elif shape_choice == 1:
        print("circle")
        for i in range(times):
            small.color(chosen_colors[i % 2])
            draw_circle(small, circleSize)
            small.right(random.randint(0, 359))

    elif shape_choice == 2:
        print("triangle")
        for i in range(times):
            small.color(chosen_colors[i % 2])
            draw_triangle(small, front)
            small.right(random.randint(0, 359))

    elif shape_choice == 3:
        print("polygon")
        sides = random.randint(3, 10)
        for i in range(times):
            small.color(chosen_colors[i % 2])
            draw_polygon(small, front, sides)
            small.right(random.randint(0, 359))

    time.sleep(10)
    small.clear()

window.exitonclick()
