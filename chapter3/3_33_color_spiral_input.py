import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["orange", "light blue", "gray", "pink", "purple", "white", "green", "yellow"]
sides = int(
    turtle.numinput("Number of sides", "How many sides do you want (1-8) ?", 4, 1, 8)
)

for x in range(360):
    t.pencolor(colors[x % colors])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
