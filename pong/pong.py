import turtle
import winsound

wn = turtle.Screen()
wn.title("Pongy Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)   #stops the window from updating

# score

score_a=0
score_b=0


#paddle A

paddle_a = turtle.Turtle()           #tutle module , Turtle class
paddle_a.speed(0)                     # starting animation speed
paddle_a.shape("square")
paddle_a.shapesize(5,1,1)
paddle_a.color("red")
paddle_a.penup()                        # no drawing while moving
paddle_a.goto(-350,0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1,outline=1)   #argument of shapesize
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball

ball =turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(0.5,0.5)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2 # here .2 means it move +ve .2pixel to x and +.2 pixel to y(up)
ball.dy = 0.2

# pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()           # we donot want to make a line  while moving
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A:0  Player B:0" ,align="center"  ,font=("Courier",20,"normal"))



# functions

#function for paddle_a

def paddle_a_up():
    y=paddle_a.ycor()
    y =y+30
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y=y-30
    paddle_a.sety(y)

# function for paddle_b

def paddle_b_up():
    y=paddle_b.ycor()
    y =y+30
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y=y-30
    paddle_b.sety(y)






# keyboard use/binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")          #on pressing the key w it move up
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#main

while True:
    wn.update()

    # move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checks

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy*(-1)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)   #SND_ASYNC is used so that there is no delay while pointing

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy =ball.dy*(-1)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = ball.dx*(-1)
        score_a = score_a+1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b) ,align="center"  ,font=("Courier",20,"normal"))
        if (score_a>score_b ) and (score_a==4):
            pen.clear()
            pen.write("A WIns",align="center"  ,font=("Courier",20,"normal"))
        if (score_a<score_b ) and (score_b==4):
            pen.clear()
            pen.write("B WIns",align="center"  ,font=("Courier",20,"normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx = ball.dx*(-1)
        score_b = score_b+1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b) ,align="center"  ,font=("Courier",20,"normal"))
        if (score_a>score_b ) and (score_a==4):
            pen.clear()
            pen.write("A WIns",align="center"  ,font=("Courier",20,"normal"))
        if (score_a<score_b ) and (score_b==4):
            pen.clear()
            pen.write("B WIns",align="center"  ,font=("Courier",20,"normal"))


    # paddle and ball collision
    if ((ball.xcor() >333 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50)):
        ball.setx(333)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ((ball.xcor() < -333 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50)):
        ball.setx(-333)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
