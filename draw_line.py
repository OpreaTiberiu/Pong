from turtle import Turtle


def draw_line(screen_y, offset):
    t = Turtle()
    t.penup()
    t.color("white")
    t.pencolor("white")
    t.goto(0, -screen_y / 2 - offset)
    t.setheading(90)
    while t.ycor() < ((screen_y / 2) + offset):
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)
    t.hideturtle()
