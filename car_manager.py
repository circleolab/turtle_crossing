from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
THE_BOTTOM = -240
THE_TOP = 240


def create():
    new_car = Turtle()
    new_car.shape("square")
    new_car.shapesize(1, 2)
    new_car.color(random.choice(COLORS))
    new_car.setheading(180)
    new_car.penup()
    new_car.car_position = random.randint(THE_BOTTOM, THE_TOP)
    new_car.goto(270, new_car.car_position)
    return new_car


class CarManager:
    """
    原本是将car_manager打造为控制单车。后面升级为车队管理
    """

    def __init__(self):
        self.car_list = []

        self.car_list.append(create())
        self.car_generate_time = 0.1
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.car_generate_time += 0.1

        if self.car_generate_time > 0.6:
            self.car_generate()
        for car in self.car_list:
            car.forward(self.speed)

    def car_generate(self):
        new_car = create()
        self.car_list.append(new_car)
        self.car_generate_time = 0.1

    def accelerate(self):
        self.speed += MOVE_INCREMENT

