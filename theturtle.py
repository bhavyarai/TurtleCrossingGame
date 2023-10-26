from turtle import Turtle


class TheTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.origin = (0, -280)
        self.goto(self.origin)
        self.setheading(90)


    def move(self):
        self.forward(10)

    # when collided with the wall
    def start(self):
        self.goto(self.origin)
