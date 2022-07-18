# Olympic logo drawer 
import turtle

def draw_olympic():
    # Base task: Write a content for function draw_olympic, that will make a drawing of olympic circles 
    # using turtle graphics and any types of loops (either while or for loop)
    # 5 Bonus points: using text input from tutlre, ask user to enter the color that he wants to use for the turtle pen color. 
    # 15 Bonus points: using examples from the chapter, add another loop into main loop and draw mini circles on the edges of the main circles
    t = turtle.Pen()
    t.speed(0)
    t.width(10)
    coordinates = [[0, 0], [-110, 0], [110, 0], [-55, -95], [55, -95]]
 
    for coordinate in coordinates:
        t.setx(coordinate[0])
        t.sety(coordinate[1])
        t.color(turtle.textinput("Olympic color", "Enter a color you want"))
        t.pendown()
        t.circle(50)
        t.penup()

    turtle.mainloop()


draw_olympic()

