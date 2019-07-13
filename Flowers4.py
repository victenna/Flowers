# Import module turtle to draw shapes 
import turtle
turtle.tracer(1)

# Function to draw a rectangle 
def draw_rectangle(some_turtle):
    for x in range(1,5):
        some_turtle.forward(50)
        if (x%2 == 1):
            some_turtle.right(60)
        else:
            some_turtle.right(120)


# Function to draw a flower
def draw_flower():
    # Creating a screen for a turtle to draw
    window = turtle.Screen()
    window.bgcolor("blue")

    # Creating a turtle object
    flower = turtle.Turtle()
    flower.shape("circle")
    flower.color("red")
    flower.speed(10)

    for i in range(1,37):
        draw_rectangle(flower)
        flower.right(10)

    flower.color("green")
    flower.right(90)
    flower.forward(200)
    
    window.exitonclick()

# Calling a function to draw a flower
draw_flower()   
