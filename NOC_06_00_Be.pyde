# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

import random
from Vehicle import Vehicle
from Food import Food
def setup():
    global vehicle
    global X
    global Y
    global food
    size(640, 360)
    velocity_vehicle = PVector(0, 0)
    velocity_food = PVector(0,0)
    vehicle = Vehicle(width / 2, height / 2, velocity_vehicle)
    X = random.randrange(1, 640)
    Y = random.randrange(1, 360)
    food = Food(X, Y, velocity_food)
    
def draw():
    background(255)
    velocity = PVector(0, 0)
    text(food.getCount(), 30, 30)
    food.update()
    food.display()
    vehicle.update()
    vehicle.display()
    if ((food.getPosition().dist(vehicle.getPosition()) > 0.5)):
        vehicle.arrive(food.getPosition())
    else:
        food.setPosition()
        
    vehicle.update()
    vehicle.display()
