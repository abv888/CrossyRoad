from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        with open("score_book.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} High Score: {self.high_score}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.level > self.high_score:
            self.high_score = self.level
            with open("score_book.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.level = 1
        self.update_scoreboard()
