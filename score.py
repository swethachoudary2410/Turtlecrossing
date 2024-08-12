from turtle import Turtle,Screen

class Score():
    def __init__(self):
        self.score = 0
        self.level = 1
       # self.score_display()
        
   # def score_display(self):
    
        #Turtle().write(f"Level: {self.level}", align ="center", font= ("ariel",14,"normal"))
         

    def inc_score(self):
        self.score +=1
        self.level +=1
        
    def final_score(self):
        return self.score