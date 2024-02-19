import time
from turtle import Screen
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

current_level = 0
record = 0

game_is_on = True

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if car_manager.detect_collision(player):
        game_is_on = False

    if player.is_at_finish():
        player.go_to_start()


screen.exitonclick()