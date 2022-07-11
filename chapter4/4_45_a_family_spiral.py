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

for x in range(100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font=("Arial", int((x+4)/4), "bold"))
    t.left(360/len(family)+2)

turtle.mainloop()
