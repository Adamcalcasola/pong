from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("PONG")

paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkeypress(fun=paddle.move_up, key="Up")
screen.onkeypress(fun=paddle.move_down, key="Down")

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)

    ball.move()

    if ball.ball.xcor() < -280:
        ball.ball.setheading(0)

    if ball.ball.xcor() > 280:
        ball.ball.setheading(180)

screen.exitonclick()
