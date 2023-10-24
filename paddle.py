from turtle import Turtle


class Paddle:
    def __init__(self):
        self.y_position = 0
        self.paddle = self.create_paddle()

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.shapesize(1, 4)
        paddle.setheading(90)
        paddle.penup()
        paddle.goto(-285, 0)
        paddle.color("white")
        return paddle

    def move_up(self):
        if self.paddle.ycor() < 240:
            self.paddle.forward(20)

    def move_down(self):
        if self.paddle.ycor() > -240:
            self.paddle.backward(20)

