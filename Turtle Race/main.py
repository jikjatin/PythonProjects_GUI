from turtle import Turtle,Screen
import random
screen= Screen()
screen.setup(width=800,height=500)          #setting screen width and height
colors=['red','blue','yellow','green','orange','brown','purple']
is_race_on=False
y=-130
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color(red,blue,yellow,green,orange,brown,purple): ")        #take user input
all_turtles=[]  
for color in colors:
  mytur= Turtle(shape='turtle') 
  mytur.penup() 
  mytur.color(color)
  mytur.goto(-380,y)               #postion turtle acc to x,y coordinates
  all_turtles.append(mytur)
  y+=50

if user_bet:
  is_race_on=True
while is_race_on:
  for turtle in all_turtles:
    random_dist=random.randint(0,10)
    turtle.fd(random_dist)
    if turtle.xcor()>380:                 #xcor gives turtle x coordinate value
      is_race_on=False
      winning_color= turtle.pencolor()              
      if winning_color==user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")  

screen.exitonclick()