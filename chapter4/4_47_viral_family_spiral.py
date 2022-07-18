import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors = ['red', 'yellow', 'green', 'blue', 'orange', 'purple', 'white', 'pink', 'gray', 'black']

family = []

name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end: ")

while name != "":
    family.append(name)
    name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] tp end: ")

for y in range(100):
    t.forward(y*4)
    position = t.position()
    heading = t.heading()
    for x in range(len(family)):
        t.pendown()
        t.pencolor(colors[x%len(family)%10])
        t.write(family[x%len(family)], font=("Arial", int((x+4)/4), "bold"))
        t.left(360/len(family)+2)
        t.width(20*x)
        t.penup()
        t.forward(x*4)
    t.setposition(position)
    t.setheading(heading)
    t.left(360/len(family)+3)

turtle.mainloop()
