from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    显示玩家的关数目，并适当提示Game Over
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 0
        self.game_up()

    def game_up(self):
        self.level += 1
        self.clear()
        self.write(f"level: {self.level}", font=FONT)

    def failed(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT)
