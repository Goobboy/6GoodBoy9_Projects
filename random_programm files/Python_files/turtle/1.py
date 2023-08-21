import turtle

Leonardo = turtle.Turtle()
#turtle.Screen() this creats the window
windows = turtle.Screen()
windows.bgcolor("Black")

####################################################################

Leonardo.color("green",)

#thinkness of the lines
Leonardo.pensize(15)
# controls the speed. range is 1-10
Leonardo.speed(3)


#####################################################################
def schildkroete():
    for i in range(5):
        Leonardo.forward(100)
        Leonardo.right(90)


schildkroete()





#this will stop closing the Turtle window
turtle.Screen().exitonclick()
#this command should be last