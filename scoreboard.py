from turtle import Turtle


FONT = ("Bebas Neue", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.clear()
        self.goto(-280, 270)
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER!", move=False, align="center", font=("Bebas Neue", 30, "normal")
        )
