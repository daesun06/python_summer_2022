# Snake Game

import turtle
import random
import time

delay = 0.1

# screen part

backgrounds = ['white', 'gray', 'pink', 'black']

screen = turtle.Screen()

def level_gen():
    screen.title("Snake Game")
    screen.bgcolor(random.choice(backgrounds))
    screen.setup(width = 600, height=600)
    screen.tracer(0) # turns off the animations

# snake head

head = turtle.Turtle()
def snake_draw(shape:str, color:str):
    head.speed(0)
    head.shape(shape)
    head.color(color)
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

# food that the snake eats W.I.P does nothing just spawns

def food_spawn(shape:str, color:str, x:int, y:int):
    food = turtle.Turtle()
    food.speed(0)
    food.shape(shape)
    food.color(color)
    food.penup()
    food.goto(x, y)

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

# game setup

level_gen()
snake_draw("square", "red")
food_spawn("circle", "orange", 80, 200)

# game loop

while True: 
    screen.update() # this makes the screen always update
    move() # using my move function to make the snake animated
    time.sleep(delay)

turtle.mainloop()