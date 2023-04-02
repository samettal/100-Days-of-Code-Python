import colorgram
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.hideturtle()
timmy.penup()
timmy.goto(-300,300)
timmy.speed(9)

COLORS_LIST = ["royalblue",'aqua',"aquamarine4","bisque4","blue violet","brown","brown1","CadetBlue1","coral4","cyan1","dark orange","DeepPink","forestgreen"]
my_colors = COLORS_LIST


def extract_color() -> list: # resimdeki en sık karşılaşılan 10 rengi tuple listesi halinde verir.
    most_frequent_colors = colorgram.extract("image.jpg", 10)
    my_colors = []
    for color in most_frequent_colors:
        my_colors.append(tuple(color.rgb))
    return my_colors

def arrange_color(my_colors): # timmy renk değiştirir.
    curr_color = random.choice(my_colors)
    return curr_color


# 4 satır 7 sütun büyüklüğünde renkleri değişen noktalar koyalım:
DOT_SIZE = 30
STEP_SIZE = 60
ROWS = 11
COLUMNS = 11
for _ in range(ROWS):
    for _ in range(COLUMNS):
        timmy.dot(size=DOT_SIZE)
        timmy.color(arrange_color(my_colors))
        timmy.penup()
        timmy.setposition(timmy.position() + (STEP_SIZE,0))
    timmy.setposition(timmy.pos() - tuple((COLUMNS * STEP_SIZE, STEP_SIZE)))


screen.exitonclick()