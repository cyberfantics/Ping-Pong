import turtle as t
from paddle import Paddle 
from ball import Ball
import time
from score import Score
from centerPoint import CenterPoint

#create screen
screen = t.Screen()
screen.bgcolor(0.5,0,0.5)
screen.setup(width=700,height=500)
screen.title('Ping Pong Game')
screen.tracer(0)

#create paddle
leftPaddle = Paddle(330)
rightPaddle = Paddle(-330)
ball = Ball()
score = Score()
center = CenterPoint()
#shape the screen
screen.listen()
screen.onkeypress(leftPaddle.goUp,'Up')  
screen.onkeypress(leftPaddle.goDown,'Down')   
screen.onkeypress(rightPaddle.goUp,'8')  
screen.onkeypress(rightPaddle.goDown,'2')  

#game logic
isGameOn = True
while isGameOn:
    screen.update()
    score.showScore()
    time.sleep(ball.ballSpeed)
    ball.move()

    if ball.ycor() >= 230 or ball.ycor()<=-230:
        ball.bounce()

    elif ball.distance(rightPaddle) < 50 and ball.xcor()<-310 or ball.distance(leftPaddle) < 50 and ball.xcor()>310 :
        ball.reverse()

    elif ball.xcor()>350 or ball.xcor()<-350:
        position = ball.xcor()
        ball.miss()
        score.increaseScore(position)

screen.exitonclick()