import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
t.width(0)
number_of_circles = int(turtle.numinput("Number of circles", "How many circles do you like in your rosette?", 6))

for x in range(number_of_circles):
    t.pencolor('red')
    t.circle(100)
    t.pencolor('yellow')
    t.circle(50)
    t.left(360/number_of_circles)

turtle.mainloop()