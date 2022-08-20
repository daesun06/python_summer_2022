import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green",
          "orange", "purple", "white", "gray"]

for n in range(50):
    t.pencolor(random.choice(colors))   
    size = random.randint(10,40)        
    sides = random.randint(3,8)
    thick = random.randint(1,6)
    t.width(thick)
    angle = t.heading()

    x = random.randrange(size,turtle.window_width()//2)
    y = random.randrange(size,turtle.window_height()//2)
    # First spiral
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 1)
    # Second spiral
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    t.setheading(180 - angle)
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 1)    
    # Third spiral
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    t.setheading(angle - 180)
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 1)
    # Fourth spiral
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    t.setheading(360 - angle)
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 1)