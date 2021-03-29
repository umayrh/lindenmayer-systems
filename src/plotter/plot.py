from turtle import *

def make_plot(turtle_str: str,
              delta: int,
              step_length: int = 10,
              initial_x: int = 0,
              initial_y: int = 0,
              drawing_speed = 10):
    clearscreen()
    penup()
    setx(initial_x)
    sety(initial_y)
    speed(drawing_speed)

    for letter in turtle_str:
        if letter in ('F', 'L', 'R'):
            pendown()
            forward(step_length)
        elif letter == 'f':
            penup()
            forward(step_length)
        elif letter == '+':
            left(delta)
        elif letter == '-':
            right(delta)
        else:
            raise RuntimeError("Bad turtle string format")
    done()
