# Snake Game

from ast import Pass
from email.errors import FirstHeaderLineIsContinuationDefect
import turtle
import random
import time

delay = 0.1

# screen part

backgrounds = ['white', 'gray', 'pink', 'black']

screen = turtle.Screen() # and if i move the "screen = turtle.Screen()" my "screen.update()" wont work also.

def level_gen():
    screen.title("Snake Game")
    screen.bgcolor(random.choice(backgrounds))
    screen.setup(width = 600, height=600)
    screen.tracer(0) # turns off the animations

# snake head

head = turtle.Turtle() # if i move the "head = turtle.Turtle()" into the function my collision detection and movement wont work :(
def spawn_snake(shape:str, color:str, x:int, y:int):
    head.speed(0)
    head.shape(shape)
    head.color(color)
    head.penup()
    head.goto(x,y)
    head.direction = "stop"

# snake body

body = []

# food that the snake eats

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

# making the score text at the top of the screen

score = ["0"]

if head.distance(food):
    turtle.penup()
    turtle.pencolor("magenta")
    turtle.setpos(x = -200, y = 270)
    turtle.pendown()
    
    turtle.write("Score = ", score)
    turtle.penup()
    turtle.hideturtle()

# game loops

while True: 
    screen.update() # this makes the screen always update

    # food collsion
    
    if head.distance(food) < 20:
        # now make the food move to a random part of the screen, after collision
        v = random.randint(-270, 270)
        l = random.randint(-270, 270)
        food.goto(v, l)
        score.append("1")
        
        # add a body part to the snake
        body_part = turtle.Turtle()
        body_part.speed(0)
        body_part.color('green')
        body_part.shape('square')
        body_part.penup()
        body.append(body_part)

    # move the end of the segments to the head

    for index in range(len(body) -1, 0, -1): # looked this up and found that doing moving the body parts in reverse is easier than the other way around.
        m = body[index - 1].xcor()
        n = body[index - 1].ycor()
        body[index].goto(m, n)

    # now we need to move the segment before the head to where the head was. otherwise it will make an error.

    if len(body) > 0:
        q = head.xcor()
        e = head.ycor()
        body[0].goto(q, e)

    # BORDER COLLISION (finnaly did it)

    if head.xcor() > 290 or head.xcor() <  -290 or head.ycor() > 290 or head.ycor() <  -290:
        # ^ - I'm sure you can do it with a different way, but this is one of the easiest
        time.sleep(1.5) # <- stops the game for 1.5 seconds
        head.goto(0, 0)
        head.direction = 'stop'
        # hiding the body parts that you had before death
        for body_part in body: 
            body_part.goto(6666, 6666) # couldn't find a way to delete the body parts, so they tp away
        body.clear()

    # making that when the snake touches the border it will reset and spawn at x:0 y:0 (a.k.a collision)
        
    move() # using my move function to make the snake animated
    
    time.sleep(delay)

turtle.mainloop()