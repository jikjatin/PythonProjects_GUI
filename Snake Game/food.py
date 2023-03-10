from turtle import Turtle
import random
class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.pu()
    self.shapesize(stretch_len=0.5,stretch_wid=0.5)
    self.color('dark goldenrod')
    self.speed('fastest')
    self.refresh()

  def refresh(self):
    rndm_cordX=random.randint(-280,280)
    rndm_cordY=random.randint(-280,280)
    self.goto(rndm_cordX,rndm_cordY)
