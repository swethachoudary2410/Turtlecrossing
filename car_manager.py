from turtle import Turtle, Screen
import time
import random

colors = ["red","blue","yellow","purple","green","orange","brown"]
 

s = Screen()
class Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 5
        self.car_list = []
    def create_cars(self):
        frequency = random.randint(1,6)
        if frequency==6:
            self.car = Turtle("square")
            self.car.shapesize(stretch_wid=1, stretch_len = 2)
            self.car.penup()
            self.car.color(random.choice(colors))
            new_y = random.randint(-220,250)
            self.car.goto(300,new_y)
            self.car_list.append(self.car)
        #time.sleep(1)

    def move(self):
        for cars in self.car_list:
            cars.penup()
            cars.backward(self.car_speed)

    def collision(self):
        self.write("Game Over", align= "center", font=("ariel",20,"normal"))
         
    def speed(self):
        self.car_speed +=5
        
         
    
        

