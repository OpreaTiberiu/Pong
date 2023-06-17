from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, speed=40):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()

        self.setheading(random.choice([x for x in range(0, 360, 15) if x not in [0, 90, 180, 270]]))
        print(self.heading())
        self.speed = speed

    def move(self):
        self.forward(self.speed)

    def turn(self):
        self.setheading(180 - self.heading())

    def bounce(self):
        self.setheading(-self.heading())

    def reset_ball(self):
        self.reset()
        self.__init__()
        self.move()
