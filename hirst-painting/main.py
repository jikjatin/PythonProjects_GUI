#Extracting colurs used in an image in the from of rgb values using colorgram library
# import colorgram
# rgb_colors=[]
# colors = colorgram.extract('img.jpg',54)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)    
import turtle as t
import random
t.colormode(255)
my_tur = t.Turtle()
my_tur.speed("fastest")
my_tur.penup()
my_tur.hideturtle()
color_list=[(237, 231, 214), (218, 234, 224), (141, 176, 206), (25, 32, 48), (28, 105, 156), (208, 161, 112), (238, 222, 234), (230, 211, 94), (131, 31, 64), (5, 162, 195), (182, 45, 84), (217, 60, 85), (226, 80, 44), (195, 129, 168), (54, 167, 116), (29, 61, 115), 
(108, 181, 91), (109, 99, 88), (2, 102, 119), (193, 187, 47), (241, 204, 1), (19, 22, 21), (52, 149, 109), (171, 211, 173), (226, 170, 186), (150, 207, 222), (234, 169, 160), (184, 186, 210), (115, 38, 37), (82, 34, 76), (122, 118, 154), (28, 28, 28)]
my_tur.setheading(225)
my_tur.forward(300)
my_tur.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    my_tur.dot(26, random.choice(color_list))
    my_tur.forward(50)

    if dot_count % 10 == 0:
        my_tur.setheading(90)
        my_tur.forward(50)
        my_tur.setheading(180)
        my_tur.forward(500)
        my_tur.setheading(0)
screen=t.Screen()
screen.exitonclick()
