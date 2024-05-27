import turtle as t
class Paddle(t.Turtle):
    def __init__(self, xCor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=3,stretch_len=0.5)
        self.goto(xCor,0)
    
    def goUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def goDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY) 

