from turtle import *

def make_plot(turtle_str: str,
              delta: int,
              step_length: int = 10,
              colors=None):
    if colors is None:
        colors = ['red', 'yellow']
    color(*colors)
    begin_fill()
    for letter in turtle_str:
        if letter == 'F':
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
    end_fill()
    done()
