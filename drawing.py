from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def rotate_left():
    timmy.left(10)


def rotate_right():
    timmy.right(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="z", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="q", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
