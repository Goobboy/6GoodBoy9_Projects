import turtle
import random
import time


def square(loop):
    for i in range(loop):
        small.forward(front)
        small.right(90)


def sircle():
    small.circle(front)

def mycircle():
    for i in range(loop):
        small.forward(front)
        small.right(front)


def triangle(wired):
    for i in range(wired):
        small.right(120)
        small.forward(front)


# def polygon():
#     for i in range(100):
#         small.forward(front)
#         small.right(angle)


def polygon(sides):
    angle = 360 / sides
    for _ in range(loop):
        small.forward(sides/100)
        small.right(angle)


now = (time.ctime())
then = (time.ctime(time.time() + 300))



small = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")


while True:
    small.pensize(random.randint(2, 4))
    small.speed(100)
    front = random.randint(80, 150)
    print(f"\nLength/radius: {front}")

    tree= random.randint(3,5)


    colour = (("cyan2", "cyan4"),("darkgoldenrod1", "darkgoldenrod"),("darkorchid2", "darkorchid4"),
              ("chocolate1","chocolate3"),("brown4", "brown3"),("darkolivegreen2","darkolivegreen4"))

    theact= colour[random.randint(0,5)]
    times = random.randint(50, 80)  # int(input("How many loops?"))
    print(f"times: {times}")

    angle = random.randint(1, 359)
    saver= 1 #random.randint(0,3)


    if saver==0:
        print("square")
        loop = random.randint(2, 7)
        print(f"end loop: {loop}")
        if random.randint(0, 3) == 1:
            print("square1")
            for i in range(int(times/3)):
                small.color(colour[random.randint(0, 5)][i % 2])
                square(loop)
                small.right(angle)

            time.sleep(3)

            for i in range(times):
                small.color(colour[random.randint(0, 5)][i % 2])
                square(loop)
                small.right(angle)

        else:
            print("square2")
            for i in range(int(times/3)):
                small.color(theact[i % 2])
                square(loop)
                small.right(angle)

            time.sleep(3)

            for i in range(times):
                small.color(theact[i % 2])
                square(loop)
                small.right(angle)

    elif saver==1:
        colt=(mycircle,)
        obama=random.choice(colt)
        print("sircle")
        loop = random.randint(5, 13)
        print(f"end loop(mycircle): {loop}")
        if random.randint(0, 3) == 1:
            print("circle1")
            for i in range(int(int(times/3))):
                small.color(colour[random.randint(0, 5)][i % 2])
                obama()
                small.right(angle)

            time.sleep(3)

            for i in range(times):
                small.color(colour[random.randint(0, 5)][i % 2])
                obama()
                small.right(angle)

        else:
            for i in range(int(int(times/3))):
                small.color(theact[i % 2])
                obama()
                small.right(angle)

            time.sleep(3)

            for i in range(times):
                small.color(theact[i % 2])
                obama()
                small.right(angle)

    elif saver==2:
        wired=random.randint(1,6)
        print(f"Wired value: {wired}")
        print("trinagle")
        if random.randint(0, 3) == 1:
            print("trinagle1")
            for i in range(int(times/3)):
                small.color(colour[random.randint(0, 5)][i % 2])
                triangle(wired)
                small.right(angle)

            time.sleep(3)

            for i in range(times):
                small.color(colour[random.randint(0, 5)][i % 2])
                triangle(wired)
                small.right(angle)

        else:
            print("trinagle2")
            for i in range(int(times/3)):
                small.color(theact[i % 2])
                triangle(wired)
                small.right(angle)

            time.sleep(3)

            for i in range(times):
                small.color(theact[i % 2])
                triangle(wired)
                small.right(angle)

    elif saver==3:
        print("polygon")
        sides = random.randint(100, 1000)
        print(f"Sides: {sides}")
        loop = random.randint(sides, sides+1)
        print(f"end loop: {loop}")

        if random.randint(0, 3) == 1:
            print(f"angle: {angle}")
            print("polygon1")

            for i in range(int(times/3)):
                small.color(colour[random.randint(0, 5)][i % 2])
                polygon(sides)
                small.right(angle)

            time.sleep(3)

            for i in range(times):
                small.color(colour[random.randint(0, 5)][i % 2])
                polygon(sides)
                small.right(angle)

        else:

            print("polygon2")
            print(f"angle: {angle}")
            for i in range(int(times/3)):
                # small.color(theact[i % 2])
                # polygon()
                # small.right(angle)

                small.color(theact[i % 2])
                polygon(sides)
                small.right(random.randint(1, 359))

            time.sleep(3)


            for i in range(times):
                # small.color(theact[i % 2])
                # polygon()
                # small.right(angle)

                small.color(theact[i % 2])
                polygon(sides)
                small.right(random.randint(1, 359))

    time.sleep(6)
    small.clear()

    if time.ctime()== then:
        break

# window.exitonclick()


