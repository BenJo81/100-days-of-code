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

go = True

while go:
    screen.colormode(255)
    color_1 = random.randint(0, 255)
    color_2 = random.randint(0, 255)
    color_3 = random.randint(0, 255)
    tim.pencolor(color_1, color_2, color_3)
    tim.pensize(15)
    tim.speed(10)
    tim.forward(30)
    move = random.randint(1, 5)
    if move == 1:
        tim.right(90)
    elif move == 2:
        tim.left(90)
    elif move == 3:
        tim.right(180)





screen.exitonclick()