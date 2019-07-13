import turtle
t=turtle.Turtle('turtle')
t.color('black','red')
turtle.tracer(0,0)
def petal(r,angle):
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)

t.begin_fill()

for q in range (16):
    t.setheading(22.5*q)
    petal(200,100)
t.end_fill()

t.color('yellow')
t.begin_fill()

for q in range (8):
    t.setheading(45*q)
    petal(180,80)
t.end_fill()

t.color('green')
t.begin_fill()

for q in range (8):
    t.setheading(45*q)
    petal(160,60)
t.end_fill()

t1=turtle.Turtle('circle')
t1.color('orange')
t1.shapesize(8)

