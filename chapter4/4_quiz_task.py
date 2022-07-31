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

    # minicoordinates = [[-110, -50,], [-135, -25], [-160, 0], [-135, 25], [-110, 50], [-85, 25], [-60, 0], [-85, -25],
    
    # [0, -50], [-25, -25], [-50, 0], [-25, 25], [0, 50], [25, 25], [50, 0], [25, -25],
    
    # [110, -50], [85, -25], [60, 0], [85, 25], [110, 50], [135, 25], [160, 0], [135, -25],
    
    # [-55, -145], [-80, -120], [-105, -95], [-80, -70], [-55, -45], [-30, -70], [-5, -95], [-30, -70],

    # [55, -145], [30, -120], [5, -95], [30, -70], [55, -45], [80, -70], [105, -95], [80, -70]]

    for coordinate in coordinates:
        t.setx(coordinate[0])
        t.sety(coordinate[1])
        t.color(turtle.textinput("Olympic color", "Enter a color you want"))
        t.pendown()
        t.circle(50)
        # for minicoordinate in minicoordinates:
        #     t.setx(minicoordinate[0])
        #     t.sety(minicoordinate[1])
        #     t.pendown()
        #     t.circle(10)
        #     t.penup()
        t.penup()

    turtle.mainloop()


draw_olympic()
