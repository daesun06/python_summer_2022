# Snake Game

from ast import Pass
from email.errors import FirstHeaderLineIsContinuationDefect
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
def spawn_snake(shape:str, color:str, x:int, y:int):
    head.speed(0)
    head.shape(shape)
    head.color(color)
    head.penup()
    head.goto(x,y)
    head.direction = "stop"

# food that the snake, now spawns in random locations

def spawn_food(shape:str, color:str, x:int, y:int):
    n = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    m = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    food = turtle.Turtle()
    food.speed(0)
    food.shape(shape)
    food.color(color)
    food.penup()
    food.goto(n, m)
    return food

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
snake_head = spawn_snake("square", "red", 0, 0)
food = spawn_food("circle", "orange", 80, 200)

# collision detection 

def collision_detection(): 
    # TODO implement collision detection
    pass

def food_collision():
    # TODO implement food collision detection
    pass

# game loops
while True: 
    screen.update() # this makes the screen always update
    move() # using my move function to make the snake animated
    time.sleep(delay)

turtle.mainloop()