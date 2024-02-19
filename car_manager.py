from turtle import Turtle
import random
from car import Car

STARING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Car()
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def detect_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def reset_manager(self):
        for car in self.cars:
            car.goto(100000, 100000)
        self.cars.clear()
        self.car_speed = STARING_MOVE_DISTANCE
