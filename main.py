import turtle
import pandas
import time
import threading

screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.setposition(250,250)
score_pen.penup()
country_csv = pandas.read_csv("50_states.csv")
screen.bgpic("blank_states_img.gif")

country_list = country_csv["state"].to_list()

score = 0

# print("there is not such country")
# user_choice = input("please choose a country").title()

input_exist = False
game_is_on = True
while game_is_on:

    score_pen.pendown()
    score_pen.clear()
    score_pen.write(f"you guessed {score}/52 states")
    user_choice = screen.textinput("country guess", "please choose a country").title()
    while not input_exist:

        if user_choice in country_list:
            selected_country = country_csv[country_csv["state"] == user_choice]
            selected_country_list = selected_country["state"].to_list()
            selected_country_x = selected_country["x"].to_list()
            selected_country_y = selected_country["y"].to_list()
            pen.setx(selected_country_x[0])
            pen.sety(selected_country_y[0])
            pen.write(selected_country_list[0])
            input_exist = True
            country_list.remove(user_choice)
            score += 1
        else:

            user_choice = screen.textinput("no such country", "please choose a country").title()
            input_exist = False
    input_exist = False

screen.exitonclick()