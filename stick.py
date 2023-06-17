from turtle import Turtle


def int_sign(x):
    if x == 0:
        return 0
    else:
        return x / abs(x)


class Stick(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.goto(x_pos, 0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=9)
        self.setheading(90)
        self.max_y_pos = y_pos

    def up(self):
        if self.ycor() < self.max_y_pos:
            self.setheading(90)
            self.forward(20)

    def down(self):
        if self.ycor() > -self.max_y_pos:
            self.setheading(270)
            self.forward(20)
