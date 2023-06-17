from turtle import Screen
from score import Score
from stick import Stick
from ball import Ball
from draw_line import draw_line
import time

SCREEN_X = 1600
SCREEN_Y = 1200
OFFSET = 100
WALL_COLLISION_DISTANCE = 10
DISTANCE_TO_STICK = 85
REFRESH_RATE = 0.001

screen = Screen()
screen.setup(SCREEN_X, SCREEN_Y)
screen.bgcolor("orange")
screen.title("Pong")
screen.tracer(0)

score = Score(SCREEN_Y, OFFSET)
draw_line(SCREEN_Y, OFFSET)

x_coord = SCREEN_X / 2 - OFFSET
y_coord = SCREEN_Y / 2 - OFFSET

left_stick = Stick(-x_coord, y_coord)
right_stick = Stick(x_coord, y_coord)

ball = Ball()

screen.listen()
screen.onkey(right_stick.up, "Up")
screen.onkey(right_stick.down, "Down")
screen.onkey(left_stick.up, "w")
screen.onkey(left_stick.down, "s")
print([x for x in range(0, 360, 15) if x not in [0, 180, 90]])
game_on = True
while game_on:
    screen.update()
    time.sleep(REFRESH_RATE)
    ball.move()
    if abs(ball.xcor()) >= x_coord - WALL_COLLISION_DISTANCE \
            and (ball.distance(left_stick) < DISTANCE_TO_STICK
                 or ball.distance(right_stick) < DISTANCE_TO_STICK):
        ball.turn()
    if ball.xcor() > x_coord + WALL_COLLISION_DISTANCE:
        ball.reset_ball()
        score.left_point()
    if ball.xcor() < -x_coord - WALL_COLLISION_DISTANCE:
        ball.reset_ball()
        score.right_point()
        if score.score_left == 10 or score.score_right == 10:
            game_on = False
    if ball.ycor() >= y_coord - WALL_COLLISION_DISTANCE or ball.ycor() <= -y_coord + WALL_COLLISION_DISTANCE:
        ball.bounce()

score.game_over()
screen.exitonclick()
