from turtle import Turtle
import random


class Dot(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.showturtle()
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-230, 230))




