from turtle import Turtle
class CenterPoint(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.pensize(6)
        self.goto(0,250)
        self.goto(0,-250)