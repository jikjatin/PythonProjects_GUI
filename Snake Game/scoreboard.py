from turtle import Turtle
FONT=('Courier', 15,'normal')
class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.score=0
    with open("./hiscore.txt") as data:
      self.high_score=int(data.read())
    self.hideturtle()
    self.pu()
    self.color('white')
    self.update()

  def update(self):
    self.clear()
    self.goto(0,275)
    self.write(f"Score: {self.score}  High Score: {self.high_score}",False,"center",font=FONT)
    

  def check_highscore(self):
    if self.score > self.high_score:
      self.high_score=self.score
      with open("./hiscore.txt",'w') as data:
        data.write(f"{self.high_score}")
    self.score=0
    self.update()    

  def inc_score(self):
    self.score+=1
    self.update() 
  # def over(self):  
  #   self.goto(0,0)  
  #   self.write("GAME OVER:(",False,"center",font=FONT)

