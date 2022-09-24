#Snake game By Sobhani Fahim
import turtle
from turtle import *
import time
from random import randint
delay=0.2
score=0
high_score=0

#Setting up Screen

win= turtle.Screen()
win.title("Snake game")
win.bgcolor("springgreen")
win.setup(width=600,height=600)
win.tracer(0)
#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("darkblue")
head.penup()
head.goto(0,0)
head.direction = "stop"
#Snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

bodysegments=[]
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score :0 High Score:0", align="center",font=("Courier",20,"italic"))
#Functions
def go_up():
    if head.direction!="down":
       head.direction = "up"
def go_down():
    if head.direction != "up":
       head.direction = "down"
def go_left():
    if head.direction != "right":
       head.direction = "left"
def go_right():
    if head.direction != "left":
       head.direction = "right"

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard bindings
win.listen()
win.onkeypress(go_up,"w")
win.onkeypress(go_down,"s")
win.onkeypress(go_left,"a")
win.onkeypress(go_right,"d")
#Main game loop

while True:
    win.update()
    #border collision check
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        #hide bodysegemnts
        for segment in bodysegments:
            segment.goto(1000,1000)
        # clear segment list
        bodysegments.clear()
        # reset score
        score = 0
        #reset delay
        delay=0.1
        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score, high_score), align="center",
                  font=("Courier", 20, "italic"))

    if head.distance(food)<20:
        #Move the food to a random position
        x= randint(-290,290)
        y= randint(-290,290)
        food.goto(x,y)

        #Adding segments
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("royalblue")
        new_segment.penup()
        bodysegments.append(new_segment)
        #Shorten delay
        delay-=0.001
        #Scoring
        score+=4
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score, high_score), align="center",
                  font=("Courier", 20, "italic"))


    #Move the end segments first in  reverse order
    for index in range(len(bodysegments)-1,0,-1):
        x=bodysegments[index-1].xcor()
        y=bodysegments[index-1].ycor()
        bodysegments[index].goto(x,y)

    #Move bodysegment 0 to head
    if len(bodysegments)>0:
        x=head.xcor()
        y=head.ycor()
        bodysegments[0].goto(x,y)
    move()
    #body collision check
    for segment in bodysegments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            # hide bodysegemnts
            for segment in bodysegments:
                segment.goto(1000, 1000)
            # clear segment list
            bodysegments.clear()
            # reset score
            score = 0
            pen.clear()
            pen.write("Score:{}  High Score:{}".format(score, high_score), align="center",
                      font=("Courier", 20, "italic"))


    time.sleep(delay)



win.mainloop()