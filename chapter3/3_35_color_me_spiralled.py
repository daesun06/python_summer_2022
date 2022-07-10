import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["orange", "light blue", "gray", "pink", "purple", "white", "green", "yellow"]

your_name = turtle.textinput("Enter your name", "What is your name?")

sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-8) ?", 4, 1, 8))

for x in range(360):
    t.pencolor(colors[x % sides])
    t.penup()
    t.forward(x * 3 / sides + x)
    t.pendown()
    t.write(your_name, font=("Arial", int((x + sides)/sides), "bold"))
    t.left(360 / sides + 1)
    t.width(x * sides / 200)