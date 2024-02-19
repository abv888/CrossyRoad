from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)
