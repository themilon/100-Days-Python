from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 21, "normal")

class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreBord()

    def update_scoreBord(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def scoreUpdate(self):
        self.score += 1
        self.clear()
        self.update_scoreBord()

