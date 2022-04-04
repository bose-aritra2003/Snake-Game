from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)  # To reduce the turtle size to 10 by 10 from 20 by 20
        self.shape("square")
        self.color("red")
        self.speed("fastest")
        self.resetFood()

    def resetFood(self):
        """
        Resets the food object to a new random location on the screen
        """
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 250)  # 250 is to prevent overlapping of food with scoreboard on top center
        self.goto(random_x, random_y)
