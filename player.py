from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def go_up(self):
        if self.ycor() != FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        else:
            pass
