from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()






screen = Screen()
screen.exitonclick()