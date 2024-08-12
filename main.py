from turtle import Turtle, Screen
from player import Player
from car_manager import Manager
from score import Score
import time

 
s = Screen()
s.tracer(0)
s.setup(width=900, height= 700)
player = Player()
car_manager = Manager()
score = Score()

s.listen()
s.onkey(player.up, "Up")

game_is_on =True
while game_is_on:
    time.sleep(0.1)
    s.update()
    car_manager.create_cars()
    car_manager.move()
    for cars in car_manager.car_list:
        if player.distance(cars) <30:
            car_manager.collision()
            game_is_on = False
        
    if player.distance(0,270) < 20:
        score.inc_score()
        player.start_again()
        car_manager.speed()

     
     



s.exitonclick()