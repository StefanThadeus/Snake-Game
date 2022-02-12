from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.color("lime")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Moves the food object to a random location"""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        self.setheading(random.randint(0, 359))
