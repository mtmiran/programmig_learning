from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1 # ball speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """reversing the direction of y by mutipling by -1. If touch in the top
        or bottom"""
        self.y_move *= -1

    def bounce_x(self):
        """reversing the direction of x by multipling by -1. If touch the
        paddle"""
        self.x_move *= -1
        self.move_speed *= 0.9 # increase ball speed every time it touch the paddle

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1 # reset ball speed
        self.bounce_x()
