import turtle as t
import random

t.colormode(255)


class Car(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.setheading(180)
        self.set_color()
        self.goto(x=300, y=random.randint(-200, 250))

    def set_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        car_color = (r, g, b)
        self.color(car_color)

    def move(self):
        self.forward(random.randint(0, 50))

#
# def create_cars():
#     loop_count = 1
#     while True:
#         if loop_count % 6 == 0:
#             car = Car()
#             car.move()