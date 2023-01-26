import turtle
import pandas
screen= turtle.Screen()

screen.title("Indian States Game")
image="India_map.gif"
screen.addshape(image)
turtle.shape(image)
indian_states=screen.textinput(title="Guess the State",prompt="Enter name of the State").title()
data=pandas.read_csv("states.csv")
print(data)
screen.exitonclick()

