import turtle
t=turtle.Turtle('circle')
t.color('black','yellow')
turtle.bgcolor('pink')
turtle.tracer(0)
t.setheading(0)
t.begin_fill()
for q in range (16):
    t.setheading(22.5*q)
    t.fd(100)
    t.left(30)
    t.fd(100)
    t.left(150)
    t.fd(100)
    t.left(30)
    t.fd(100)
t.end_fill()
t.color('orange')
t.shapesize(8)


