from turtle import Screen, Turtle
from snake import Snake
import time

# screen options
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create snake oject
snake = Snake()


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








screen.exitonclick()
