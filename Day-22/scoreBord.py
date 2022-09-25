from turtle import Turtle

PLACEMENT = "center"
FONTS = ("Courier", 41, "normal")


class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreBord()

    def update_scoreBord(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=PLACEMENT, font=FONTS)
        self.goto(100, 200)
        self.write(self.right_score, align=PLACEMENT, font=FONTS)

    def left_point(self):
        self.left_score += 1
        self.update_scoreBord()

    def right_point(self):
        self.right_score += 1
        self.update_scoreBord()
