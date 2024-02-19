from turtle import Turtle
import random
from car import Car

STARING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Car()
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARING_MOVE_DISTANCE)

    def detect_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                print("COLLISION")
                return True

