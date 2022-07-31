# Olympic logo drawer 
import turtle
from time import sleep


def draw_generic_circle(t: turtle.Pen, x: int, y: int, radius: int):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.circle(radius)
    t.penup()

# "up", 'down', 'left', 'right'
def draw_mini_circle(t: turtle.Pen, x: int, y: int, direction: str):
    if direction == 'up':
        draw_generic_circle(t, x, y + 100 - 20, 20)
    elif direction == 'down':
        draw_generic_circle(t, x, y - 20, 20)
    elif direction == 'left':
        draw_generic_circle(t, x - 50, y + 50 - 20, 20)
    else:
        draw_generic_circle(t, x + 50, y + 50 - 20, 20)
            

def draw_olympic():
    # Base task: Write a content for function draw_olympic, that will make a drawing of olympic circles 
    # using turtle graphics and any types of loops (either while or for loop)
    # 5 Bonus points: using text input from tutlre, ask user to enter the color that he wants to use for the turtle pen color. 
    # 15 Bonus points: using examples from the chapter, add another loop into main loop and draw mini circles on the edges of the main circles
    t = turtle.Pen()
    t.speed(0)
    t.width(10)

    coordinates = [[0, 0], [-110, 0], [110, 0], [-55, -95], [55, -95]]

    directions = ['up', 'down', 'left', 'right']

    for coordinate in coordinates:
        t.setx(coordinate[0])
        t.sety(coordinate[1])
        t.color('red')
        t.pendown()
        t.circle(50)
        t.penup()
        t.width(6)
       
        for direction in directions:
            draw_mini_circle(t, coordinate[0], coordinate[1], direction)
            sleep(4)

    turtle.mainloop()


draw_olympic()
