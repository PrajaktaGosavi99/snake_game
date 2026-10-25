from turtle import Turtle
import random


class Food(Turtle):
    """A small blue dot that jumps to a random spot whenever it is eaten."""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Move the food to a new random position."""
        x_random = random.randint(-250, 250)
        y_random = random.randint(-250, 250)
        self.goto(x_random, y_random)
