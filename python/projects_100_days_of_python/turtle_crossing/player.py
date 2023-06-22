from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.position = position
        self.goto(self.position)
        

    # control turtle 
    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
               

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    # reset position
    def reset_player(self):
        self.goto(self.position)

    # detect finish FINISH_LINE
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

