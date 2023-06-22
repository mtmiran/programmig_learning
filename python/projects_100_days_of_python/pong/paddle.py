from turtle import Turtle

WIDTH = 20
HEIGHT = 100
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # control Paddle
    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)
               

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

