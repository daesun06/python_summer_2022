from re import S
import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2, 2, 2)
t.bgcolor("gray")
t.pencolor("red")
def up():
    t.forward(50)
def left():
    t.left(45)
def right(): 
    t.right(45)
def cursor(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
def thicker():
    t.width(t.width + 1)
def thinner():
    t.width(t.width - 1)
turtle.onscreenclick(up, "Up")
turtle.onscreenclick(left, "Left")
turtle.onscreenclick(right, "Right")
turtle.onscreenclick(thicker, "W")
turtle.onscreenclick(thinner, "T")
turtle.onscreenclick(cursor)