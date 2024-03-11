from turtle import Turtle,Screen
import random


screen = Screen()
is_race_on = False

screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle_list = []


for i in range(0, 6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()