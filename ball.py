from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = self.create_ball()
        self.trajectory = 0

    def create_ball(self):
        new_ball = Turtle("circle")
        new_ball.penup()
        new_ball.setheading(180)
        new_ball.color("white")

        return new_ball

    def move(self):
        self.ball.forward(20)
