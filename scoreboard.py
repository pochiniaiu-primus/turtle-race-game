from turtle import Turtle
FONT_GAME_OVER = ("Courier", 24, "bold")
ALIGNMENT = "center"
FONT_LEVEL = ("Courier", 15, "bold")


# Level: 2
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT_GAME_OVER)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT_LEVEL)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
