import turtle as t
import random

timmy = t.Turtle()
timmy.pensize(5)
timmy.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

direction = [0, 90, 180, 270]

for i in range(1000):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))