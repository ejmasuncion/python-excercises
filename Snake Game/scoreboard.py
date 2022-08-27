from ctypes import alignment
from tkinter import font
from turtle import Turtle

ALINGMENT = 'center'
FONT = ('Arial', 10, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align =  ALINGMENT, font = FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align = ALINGMENT, font = FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode = 'w') as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align = ALINGMENT, font = FONT)