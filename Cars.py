from turtle import Turtle
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

colors = ["red", "blue", "yellow", "green", "purple"]
speed = [5, 10]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(colors))
        self.shape("square")
        self.speed("slowest")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(LEFT)
        self.speed = random.choice(speed)
        self.x = 0
        self.y = 0

    def set_x(self):
        r = random.randint(0, 1)
        if r == 0:
            self.setheading(LEFT)
            self.x = 0

        if r == 1:
            self.setheading(RIGHT)
            self.y = 0

    def set_y(self):
        pass

    def move(self):
        self.fd(1)