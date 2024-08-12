from turtle import Turtle, Screen
position = (0,-270)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        #self.hideturtle()
        self.penup()
        self.setheading(90)
        self.start_again()
        
    def up(self):
        new_y = self.ycor()+10
        self.goto(self.xcor(), new_y)

    def start_again(self):
        self.goto(position)
         
         
         