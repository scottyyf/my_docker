from turtle import *

tur = Turtle()
screen =tur.getscreen()
tur.forward(100)
tur.right(90)
tur.forward(100)
tur.right(90)
tur.forward(100)
tur.right(90)
tur.forward(100)
tur.right(90)

tur.penup()
tur.goto(-200,100)
tur.pendown()

tur.color('red')
tur.fillcolor('green')
tur.begin_fill()

lst = [0, 1, 2, 3]

for i in lst:
    tur.forward(100)
    tur.left(120)
tur.end_fill()

tur.begin_fill()
tur.forward(100)
tur.left(120)
tur.forward(100)
tur.left(120)
tur.end_fill()

tur.penup()
tur.goto(200,200)
tur.pendown()
tur.fillcolor('purple')
tur.begin_fill()
for i in range(6):
    tur.forward(50)
    tur.left(60)


tur.end_fill()

tur.penup()
tur.goto(100,100)
tur.pendown()
tur.fillcolor('yellow')
tur.begin_fill()
for i in range(9):
    tur.forward(50)
    tur.left(40)
tur.end_fill()
screen.exitonclick()