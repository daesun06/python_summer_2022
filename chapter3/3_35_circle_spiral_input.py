import turtle
t = turtle.Pen()
t.speed(0)

sides = int(turtle.numinput("Number of sides", "How many sides do you want? (1-8)", 5, 1, 8))

for x in range(360):
    t.circle(x * 3 / sides + x)
    t.left(360 / sides + 1)



turtle.mainloop()