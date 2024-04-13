from turtle import Turtle
FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"


# Level: 2
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
