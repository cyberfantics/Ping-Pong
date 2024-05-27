FONT = ('Arial',20,'bold')
ALIGN = 'center'

from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.lscore = 0 
        self.rscore = 0
        self.showScore()
    
    def showScore(self):
        self.clear()
        self.goto(-50,220)
        self.write(self.lscore,align=ALIGN,font=FONT)
        self.goto(50,220)
        self.write(self.rscore,align=ALIGN,font=FONT)

    def increaseScore(self,position):
        if position>0:
            self.lscore+=1
        else:
            self.rscore+=1
        self.showScore()