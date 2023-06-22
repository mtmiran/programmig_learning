# import librarys
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create secreen game
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# create paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

# create ball
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()

# paddle movimentation
# right paddle
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# left paddle
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


# start game
game_is_on = True
while game_is_on:
    # reduce the ball speed
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # detect collision wth paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # detect l paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

# exit screen only when click
screen.exitonclick()
