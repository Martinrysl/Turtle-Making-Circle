import turtle as t
from turtle import Screen
import random

timmy_the_turtle = t.Turtle()
t.colormode(255)
timmy_the_turtle.shape('turtle')
timmy_the_turtle.width(1)
timmy_the_turtle.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)


#figura = 2
#colours = ['gray0', 'brown', 'red', 'blue', 'wheat', 'gold', 'DarkOrange', 'navy']
#for _ in range(8):
    #figura += 1

    #for x in range(figura):
     #   timmy_the_turtle.right(360/figura)
      #  timmy_the_turtle.forward(100)



#
#
#directions = [0, 90, 180, 270]
#value = random.random()
#for _ in range(100):
#    timmy_the_turtle.color(random_color())
#    timmy_the_turtle.forward(30)
#    timmy_the_turtle.setheading(random.choice(directions))













screen = Screen()
screen.exitonclick()














