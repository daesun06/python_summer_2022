import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = eval( input("Choose and enter a number between 2 and 6: "))
colors = ["pink", "light blue", "orange", "white", "gray", "purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(3*x / sides+x)
    t.left(360 / sides + 1)
    t.width(x * sides / 100)