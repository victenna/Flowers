import turtle
wn=turtle.Screen()
wn.bgcolor('yellow')
turtle.tracer(0,0)
def petal(t,r,angle):
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)

def flower(t,n,r,angle):
    for i in range(n):
        petal(t,r,angle)
        t.left(360/n)

sam=turtle.Turtle()
sam.speed(0.0)
sam.color('green')
sam.shape('turtle')
sam.up()
sam.goto(-200,200)
sam.down()
sam.begin_fill()
flower(sam,7,100,60)
sam.end_fill()

sam.color('red')
sam.up()
sam.goto(0,0)
sam.down()
sam.begin_fill()
flower(sam,10,100,80)
sam.end_fill()

sam.color('blue')
sam.up()
sam.goto(200,-200)
sam.down()
sam.begin_fill()
flower(sam,14,100,50)
sam.end_fill()

sam.color('purple')
sam.up()
sam.goto(-200,-200)
sam.down()
sam.begin_fill()
flower(sam,12,100,60)
sam.end_fill()

sam.color('brown')
sam.up()
sam.goto(200,200)
sam.down()
sam.begin_fill()
flower(sam,24,100,50)
sam.end_fill()

         
  



      
            

