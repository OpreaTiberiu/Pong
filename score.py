from turtle import Turtle
import random


class Score(Turtle):
    def __init__(self, screen_y, offset):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.pencolor("white")
        self.penup()
        self.goto(0, screen_y / 2 - offset)
        self.show_score()
        self.hideturtle()

    def update(self, left_point=False, right_point=False):
        if left_point:
            self.score_left += 1
        if right_point:
            self.score_right += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"{self.score_left}     {self.score_right}",
                   font=("Arial", 30, "normal"),
                   align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   font=("Arial", 30, "normal"),
                   align="center")

    def right_point(self):
        self.score_right += 1
        self.show_score()

    def left_point(self):
        self.score_left += 1
        self.show_score()
