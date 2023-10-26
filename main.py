from turtle import Screen
from theturtle import TheTurtle
from car import Car
from scorboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Capstone : The turtle crossing")
screen.tracer(0)

tim = TheTurtle()
level = ScoreBoard()

cars = []
num_of_cars = 10

for _ in range(num_of_cars):
    new_car = Car()
    cars.append(new_car)

screen.listen()
screen.onkey(fun=tim.move, key="Up")

game_is_on = True
loop_count = 0

while game_is_on:
    time.sleep(level.car_speed)
    screen.update()

    for car in cars:
        if car.xcor() < -300:
            car.goto(300, car.ycor())

        if car.distance(tim.position()) < 40:
            print("GAME OVER")
            level.game_over()
            game_is_on = False
        car.move()
        screen.update()

    # race completed
    if tim.ycor() > 280:
        tim.start()
        level.update_level()

screen.exitonclick()
