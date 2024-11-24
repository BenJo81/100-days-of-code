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



for shape in range(3, 11):
    complete = 0
    screen.colormode(255)
    color_1 = random.randint(1, 255)
    color_2 = random.randint(1, 255)
    color_3 = random.randint(1, 255)
    tim.pencolor(color_1, color_2, color_3)
    angle = 360 / shape
    for _ in range(shape):
        tim.forward(100)
        tim.right(angle)




screen.exitonclick()