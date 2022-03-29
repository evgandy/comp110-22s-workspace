"""Exercise 04: Turtle Scene."""

__author__ = "730227972"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my forest scene."""
    draw: Turtle = Turtle() 
    paint_square(draw, 90, 240, 80) 
    paint_square(draw, -110, 240, 80)
    paint_square(draw, 190, 240, 80)
    paint_square(draw, -210, 240, 80)
    paint_rectangle(draw, 100, 10, 50, -150)
    paint_rectangle(draw, -100, 10, 50, -150)
    paint_rectangle(draw, 200, 10, 50, -150)
    paint_rectangle(draw, -200, 10, 50, -150)
    paint_sun(draw, -350, 300, 80)
    paint_grass(draw, -450, 10, 2000, 400)
    something_fun(draw, -350, 300, 80)
    done()


def paint_square(draw: Turtle, x: float, y: float, width: float) -> None: 
    """Painting the squares of the tree tops."""
    draw.hideturtle()
    draw.color("green")
    draw.penup()
    draw.goto(x, y)
    draw.setheading(0.0) 
    draw.pendown() 
    draw.begin_fill() 
    i: int = 0 
    while i < 4:
        draw.forward(width)
        draw.right(90)
        i = i + 1
    draw.end_fill()


def paint_rectangle(draw: Turtle, x: float, y: float, width: float, length: float) -> None: 
    """Painting the rectangles of the tree trunks."""
    draw.hideturtle()
    draw.color("brown")
    draw.penup()
    draw.goto(x, y)
    draw.setheading(0.0) 
    draw.pendown()
    draw.begin_fill() 
    i: int = 0
    while i < 2: 
        draw.forward(width)
        draw.right(90) 
        draw.forward(length)
        draw.right(90)
        i = i + 1
    draw.end_fill() 


def paint_sun(draw: Turtle, x: float, y: float, width: float) -> None: 
    """Painting the square for the forest sun."""
    draw.hideturtle()
    draw.color("yellow")
    draw.penup()
    draw.goto(x, y)
    draw.setheading(0.0)
    draw.pendown()
    draw.begin_fill() 
    i: int = 0
    while i < 4:
        draw.forward(width)
        draw.right(90)
        i = i + 1
    draw.end_fill() 


def paint_grass(draw: Turtle, x: float, y: float, width: float, length: float) -> None: 
    """Painting the grass underneath the trees."""
    draw.hideturtle()
    draw.color("green")
    draw.penup()
    draw.goto(x, y)
    draw.setheading(0.0) 
    draw.pendown()
    draw.begin_fill() 
    i: int = 0
    while i < 2: 
        draw.forward(width)
        draw.right(90) 
        draw.forward(length)
        draw.right(90)
        i = i + 1
    draw.end_fill() 


def something_fun(draw: Turtle, x: float, y: float, width: float) -> None:
    """Trying something fun by making the sun shine."""
    draw.color("orange")
    draw.penup()
    draw.goto(x, y)
    draw.setheading(0.0)
    draw.pendown()

    SHRINK_BY_FACTOR = 0.96
    i: int = 0 
    while i < 40:
        draw.forward(width)
        draw.right(93)
        i = i + 1
        width = width * SHRINK_BY_FACTOR 


if __name__ == "__main__":
    main() 