import turtle
import random
t=turtle.Turtle()
turtle.bgcolor("orange")
t.shape("circle")
t.pencolor("white")
def simpson():
    t.pendown()
    t.speed(10)
    l_eye()
    r_eye()
    head()
    mouth()
    t.penup()
    t.goto(0,0)
    t.setheading(0)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    ear()
    t.penup()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.backward(25)
    t.pendown()
    hair_1()
    t.penup()
    t.setheading(0)
    t.goto(0,0)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.right(120)
    t.pendown()
    hair_2()
    t.penup()
    t.left(90)
    t.backward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.pendown()
    hair_2()
    
def r_eye():
    t.left(90)
    t.color("black", "white")
    t.begin_fill()
    t.pendown()
    t.pen(pensize=5)
    counter=0
    while(counter<360):
        t.forward(1)
        t.right(1)
        counter=counter+1
    t.end_fill()
    t.penup()
    t.right(60)
    t.forward(50)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    counter2=1
    while(counter2<=360):
        t.forward(3)
        t.right(20)
        counter2=counter2+18
    t.end_fill()
    t.penup()
    t.backward(50)
    t.setheading(0)
    

def l_eye():
    t.color("black", "white")
    t.begin_fill()
    t.pendown
    t.pen(pensize=5)
    counter=1
    while(counter<=360):
        t.forward(1)
        t.right(1)
        counter=counter+1
    t.end_fill()
    t.penup()
    while(counter>=300):
        t.backward(1)
        t.left(1)
        counter=counter-1
    t.right(90)
    t.forward(20)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    counter2=1
    while(counter2<=360):
        t.forward(3)
        t.right(20)
        counter2=counter2+18
    t.end_fill()
    t.penup()
    t.backward(20)
    t.left(90)
    while(counter>=270):
        t.backward(1)
        t.left(1)
        counter=counter-1
    t.setheading(0)
    t.right(10)
    t.forward(110)
    t.setheading(0)

def curveright(frwrd, turn, angle, increment):
    counter4=0
    while(counter4<angle):
        t.right(turn)
        t.forward(frwrd)
        counter4=counter4+increment

def curveleft(frwrd, turn, angle, increment):
    counter4=0
    while(counter4<angle):
        t.left(turn)
        t.forward(frwrd)
        counter4=counter4+increment

def head():
    t.forward(7)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.pendown()
    t.color("black", "#FFD90F")
    t.begin_fill()
    t.forward(60)
    counter3=1
    while(counter3<=180):
        t.left(2)
        t.forward(1)
        counter3=counter3+2
    counter3=0
    while(counter3<=10):
        t.forward(3)
        t.left(1)
        counter3=counter3+1
    t.forward(20)
    counter3=0
    while(counter3<=90):
        t.right(1)
        t.forward(1)
        counter3=counter3+1
    t.forward(20)
    counter3=0
    while(counter3<=90):
        t.right(1)
        t.forward(1)
        counter3=counter3+1
    t.forward(5)
    counter3=0
    while(counter3<=75):
        t.right(1)
        t.forward(1)
        counter3=counter3+1
        counter3=counter3+1
    t.forward(30)
    t.setheading(0)
    t.right(90)
    t.forward(30)
    curveright(1, 2, 30, 1)
    t.setheading(0)
    t.forward(225)
    t.left(110)
    curveright(6, 1, 30, 1)

    t.forward(200)
    curveleft(2, 1, 180, 1)
    t.forward(105)
    curveright(1, 2, 10, 1)
    t.left(135)
    curveright(1, 1, 83, 1)
    t.left(135)
    curveright(1, 1, 310, 1)
    t.end_fill()

def mouth():
    t.penup()
    t.goto(0,0)
    t.setheading(0)
    t.right(90)
    t.forward(145)
    t.left(90)
    t.pendown()
    t.color("black", "#D1B270")
    t.begin_fill()
    t.forward(20)
    t.left(37)
    counter3=0
    while(counter3<=90):
        t.right(1)
        t.forward(1)
        counter3=counter3+1
    t.forward(20)
    counter3=0
    while(counter3<=90):
        t.right(1)
        t.forward(1)
        counter3=counter3+1
    t.forward(5)
    counter3=0
    while(counter3<=90):
        t.right(1)
        t.forward(1)
        counter3=counter3+2
    t.right(10)
    t.forward(75)
    curveright(1, 5, 40, 1)
    counter3=0
    while(counter3<10):
        t.left(5)
        t.backward(1)
        counter3=counter3+1
    t.left(60)
    curveleft(2, 0.5, 20, 0.5)
    t.end_fill()

def ear():
    t.color("black", "#FFD90F")
    t.begin_fill()
    curveleft(0.5, 1, 180, 1)
    t.penup()
    t.left(90)
    t.forward(10)
    t.left(90)
    t.pendown()
    curveright(0.25, 1, 180, 1)
    t.end_fill()

def hair_1():
    t.left(90)
    t.right(30)
    t.forward(60)
    t.left(30)
    t.backward(55)
    t.right(60)
    t.forward(50)
    t.left(30)
    t.backward(60)

def hair_2():
    t.left(90)
    curveright(1, 1, 180, 1)
    t.forward(10)

simpson()    