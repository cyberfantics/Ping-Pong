import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.ballSpeed = 0.2
        self.shapesize(1,1)
    
    def move(self):
        newX = self.xcor()+self.xmove
        newY = self.ycor()+self.ymove
        self.goto(newX,newY)
    
    def bounce(self):
        self.ymove *= -1
    
    def reverse(self):
        self.xmove *= -1
        self.ballSpeed *= 0.9

    def miss(self):
        self.goto(0,0)
        self.reverse()
        self.ballSpeed = 0.2
        self.move()
    