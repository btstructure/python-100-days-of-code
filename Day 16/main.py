# import turtle

# timmy = turtle.Turtle()

from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color('coral')
my_screen = Screen

print(my_screen.canvheight)
#screen will only close/end when it is closed out
my_screen.exitonclick()

