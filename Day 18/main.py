from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
screen = Screen()
# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

go = 0

while go < 360:
    screen.colormode(255)
    color_1 = random.randint(0, 255)
    color_2 = random.randint(0, 255)
    color_3 = random.randint(0, 255)
    tim.pencolor(color_1, color_2, color_3)
    tim.circle(100)
    tim.right(10)
    tim.speed("fastest")
    go += 10





screen.exitonclick()