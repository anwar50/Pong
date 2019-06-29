#Simple Python project
#By @AnwarAbdi
#Functional style

import turtle

#features of window!
wind = turtle.Screen()
wind.title("Pong game by @Anwar!")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)  #vertically centered on the left side of the screen

#Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)  #vertically centered on the right side of the screen

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)  #vertically centered on the right side of the screen
    #ball moves by two pixels!
ball.dx = 2
ball.dy = 2

#Ball2
ball_two = turtle.Turtle()
ball_two.speed(0)
ball_two.shape("circle")
ball_two.color("white")
ball_two.penup()
ball_two.goto(0, 0)  #vertically centered on the right side of the screen
    #ball moves by two pixels!
ball_two.dx = 2
ball_two.dy = 2

#Track of score!
score_One = 0
score_two = 0

#Pen FOR SCORING 
pen = turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write("Player One: {}  Player Two: {}".format(score_One, score_two), align="center", font=("Courier", 24, "normal"))

#functions to move the paddles up or down
def paddle_A_up():
        #coordinates of the paddle
    y = paddle_A.ycor()
    y+=20
    paddle_A.sety(y)

def paddle_A_down():
        #coordinates of the paddle 
    y = paddle_A.ycor()
    y-=20
    paddle_A.sety(y)

def paddle_B_up():
        #coordinates of the paddle
    y = paddle_B.ycor()
    y+=20
    paddle_B.sety(y)

def paddle_B_down():
        #coordinates of the paddle 
    y = paddle_B.ycor()
    y-=20
    paddle_B.sety(y)


#Keyboard bind through turtle
wind.listen()
wind.onkeypress(paddle_A_up, "w")
wind.onkeypress(paddle_A_down, "s")

wind.onkeypress(paddle_B_up, "Up")
wind.onkeypress(paddle_B_down, "Down")

#Main game!
while True:
 wind.update()
 #Move the first ball
 ball.setx(ball.xcor() + ball.dx)
 ball.sety(ball.ycor() + ball.dy)
 #Move the second ball
 ball_two.setx(ball_two.xcor() + ball_two.dx)
 ball_two.sety(ball_two.ycor() + ball_two.dy)

    #border checks & reverse direction
 if ball.ycor() > 290:
     ball.sety(290)
     ball.dy *= -1
 if ball.ycor() < -290:
     ball.sety(-290)
     ball.dy *= -1
 if ball.xcor() > 390:
     ball.goto(0, 0)
     ball.dx *= -1 
     score_One += 1
     pen.clear()
     pen.write("Player One: {}  Player Two: {}".format(score_One, score_two),  align="center", font=("Courier", 24, "normal"))

 if ball.xcor() < -390:
     ball.goto(0, 0)
     ball.dx *= -1
     score_two += 1
     pen.clear()
     pen.write("Player One: {}  Player Two: {}".format(score_One, score_two),  align="center", font=("Courier", 24, "normal"))

    #border checks & reverse direction for ball two
 if ball_two.ycor() > 290:
     ball_two.sety(290)
     ball_two.dy *= -1
 if ball_two.ycor() < -290:
     ball_two.sety(-290)
     ball_two.dy *= -1
 if ball_two.xcor() > 390:
     ball_two.goto(0, 0)
     ball_two.dx *= -1 
     score_One += 1
     pen.clear()
     pen.write("Player One: {}  Player Two: {}".format(score_One, score_two),  align="center", font=("Courier", 24, "normal"))
 if ball_two.xcor() < -390:
     ball_two.goto(0, 0)
     ball_two.dx *= -1
     score_two += 1
     pen.clear()
     pen.write("Player One: {}  Player Two: {}".format(score_One, score_two),  align="center", font=("Courier", 24, "normal"))
     #Paddle and ball collision PADDLE B
 if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor()-40):
     ball.setx(340)
     ball.dx *= -1
 if (ball_two.xcor() > 340 and ball_two.xcor() < -50) and (ball_two.ycor() < paddle_B.ycor() + 40 and ball_two.ycor() > paddle_B.ycor()-40):
     ball_two.setx(340)
     ball_two.dx *= -1
    #Paddle and ball collision PADDLE A
 if (ball.xcor() > -340 and ball.xcor() < -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor()-40):
     ball.setx(-340)
     ball.dx *= -1
 if (ball_two.xcor() > -340 and ball_two.xcor() < -350) and (ball_two.ycor() < paddle_A.ycor() + 40 and ball_two.ycor() > paddle_A.ycor()-40):
     ball_two.setx(-340)
     ball_two.dx *= -1


