import turtle
import pandas
screen= turtle.Screen()
my_tur=turtle.Turtle()
screen.title("Indian States Game")
image="India_map.gif"
screen.addshape(image)
my_tur.shape(image)

data=pandas.read_csv("states.csv")
for state in data['state']:
  indian_states=str(screen.textinput(title="Guess the State",prompt="Enter name of the State")).title()    
  if indian_states==state:
    my_tur.goto(int(data['x']),int(data['y']))
    my_tur.write(f"{state}")
    


screen.exitonclick()

