from turtle import Turtle
FONT = ('Courier', 25, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.updateScore()

    def showScore(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.showScore()

    def updateScore(self):
        self.score += 1
        self.showScore()


