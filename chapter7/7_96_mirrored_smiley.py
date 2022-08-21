# So, beacuse the turtle.onscreenclick() and turtle.onscreenclick() function's doesn't work for me. I'm going 
# to change this program a little bit.
import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.hideturtle()
def draw_smiley(x,y):      
    t.penup()
    t.setpos(x,y)
    t.pendown()
    # Head
    t.pencolor("gray")
    t.fillcolor("gray")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    # Left eye
    t.setpos(x-15, y+60)
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # Right eye
    t.setpos(x+15, y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # Mouth
    t.setpos(x-25, y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)

for n in range(50):    
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    draw_smiley(x, y)
    draw_smiley(-x, y)
    draw_smiley(x, -y)
    draw_smiley(-x, -y)
