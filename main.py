import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=600)
screen.title("Turtle crossing")
screen.tracer(0)


# Create and turtle
tim = Player()
screen.listen()
screen.onkeypress(tim.move, "Up")

# Create scoreboard
score = Scoreboard()

# Create a car
car_manager = CarManager()


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    # Keep moving cars
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision
    for car in car_manager.all_cars:  # Loop through all cars
        if tim.distance(car) < 20:
            game_is_on = False
            score.game_over()

    # Level up
    if tim.ycor() > 280:
        tim.start()
        score.level_up()
        car_manager.car_level_up()


screen.exitonclick()
