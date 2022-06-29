import turtle
t = turtle.Pen()
turtle.bgcolor("pink")
t.pencolor("white")
t.speed(0)
for x in range(10000):
    t.circle(x)
    t.left(90)

turtle.mainloop()