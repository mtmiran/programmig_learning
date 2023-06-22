import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create turtle
turtle_player = Player((0,-280))

# create cars
car_manager = CarManager()

# create scoreboard
scoreboard = Scoreboard()

# move turtle 
screen.listen()
screen.onkey(turtle_player.up, "Up")
screen.onkey(turtle_player.down, "Down")

# start game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    
    # detect colision
    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20: 
            game_is_on = False
            scoreboard.game_over()

    # detect finish line
    if turtle_player.is_at_finish_line():
        turtle_player.reset_player()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
