from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.car_speed = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.car_speed *= 0.9
        self.goto(x=-240, y=250)
        self.write(arg=f"Level:{self.level}", align="center", font=("courier", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("courier", 18, "normal"))
