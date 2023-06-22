from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time

# screen options
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create snake oject
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# control the snake with a keypress
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    # avoid frame delay
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  
        snake.extend()
        scoreboard.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # detect collision with tail
    # passing over the snake head - segments[1:]
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# exit the screen with click
screen.exitonclick()
