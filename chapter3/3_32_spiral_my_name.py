# Not a programming challenge.

                # Set up turtle graphics.

import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ("red", "yellow", "green", "blue")

# Ask the user's name using turtle's textinput pop-op window.
your_name = turtle.textinput("Enter your name", "What is your name?")

# Draw a spiral of the name on the screen, written 100 times.
for x in range(100):
    t.pencolor(colors[x % 4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(your_name, font=("Arial", int((x + 4)/4), "bold"))
    t.left(92)


turtle.mainloop()