from turtle import Turtle


def draw_black_squares(start_coordinates):
    turtle = Turtle()
    turtle.speed('fastest')
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(start_coordinates)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()


def draw_white_squares(start_coordinates):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(start_coordinates)
    turtle.pendown()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)


def draw_dead_line(x_start, window_height):
    dead_line = Turtle()
    dead_line.color('red')
    dead_line.hideturtle()
    dead_line.speed('fastest')
    dead_line.penup()
    dead_line.goto(x_start, window_height / 2)
    dead_line.pendown()
    dead_line.fillcolor("red")
    dead_line.begin_fill()
    dead_line.right(90)
    dead_line.forward(window_height)
    dead_line.right(90)
    dead_line.forward(20)
    dead_line.right(90)
    dead_line.forward(window_height)
    dead_line.right(90)
    dead_line.forward(20)
    dead_line.end_fill()


def draw_end_line(rat_length, screen):
    end_line = Turtle()
    end_line.hideturtle()
    end_line.penup()
    end_line.goto(screen.window_width() / 2 - rat_length, screen.window_height() / 2)
    end_line.right(90)
    checker = screen.window_height()
    while checker > 0:
        draw_black_squares(end_line.pos())
        draw_white_squares(end_line.pos())
        end_line.forward(20)
        checker = checker - 20


