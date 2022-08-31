# Snake Game

import turtle
import random
import time

delay = 0.1

# screen part

backgrounds = ['white', 'gray', 'pink', 'black']

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor(random.choice(backgrounds))
screen.setup(width = 600, height=600)
screen.tracer(0) # turns off the animations

# snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food that the snake eats W.I.P does nothing just spawns

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0, 200)

# making the snake controlable

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction =="right":
        x = head.xcor()
        head.setx(x + 20)

# controls

turtle.listen()
turtle.onkeypress(go_up, "Up")
turtle.onkeypress(go_down, "Down")
turtle.onkeypress(go_left, "Left")
turtle.onkeypress(go_right, "Right")

# game loop

while True: 
    screen.update() # this makes the screen always update

    move() # using my move function to make the snake animated

    time.sleep(delay)

turtle.mainloop()