from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
all_turtles = []

for i in range(0, 6):
    color = colors[i]
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, (-100 + 40 * i))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won, {winning_color} turtle won!!!")
            else:
                print(f"You've lost , {winning_color} turtle won!!!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()