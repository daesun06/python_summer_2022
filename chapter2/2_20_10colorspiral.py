import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 7
colors = ["red", "yellow", "green", "blue", "light blue", "orange", "pink", "white", "gray", "purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(3*x / sides+x)
    t.left(360 / sides + 1)
    t.width(x * sides / 100)
turtle.mainloop()