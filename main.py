from turtle import Screen, Turtle
from Cars import Car
from Player import Player
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

HEIGHT = 600
WIDTH = 600

screen = Screen()
screen.setup(HEIGHT, WIDTH)
screen.tracer(0)

car = Car()
player = Player()
roadslen = []

def roads():
    road = Turtle()
    road.penup()
    road.setpos(WIDTH/2, HEIGHT/2)
    road.setheading(LEFT)
    step = HEIGHT/2
    distance = 5
    for i in range(HEIGHT//20):
        for i in range(WIDTH//distance):
            road.pendown()
            road.fd(distance)
            road.penup()
            road.fd(distance)
        step -= 20
        road.setpos(WIDTH/2, step)
        roadslen.append(1)

roads()
print(len(roadslen))

def main():
    game_on = True
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")
    while game_on:
        screen.update()
        car.move()
        time.sleep(0.02)


screen.listen()
main()
screen.exitonclick()