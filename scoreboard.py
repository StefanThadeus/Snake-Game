from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 265)
        self.score = 0
        self.show_score()

    def show_score(self):
        """Renders the score message on screen"""
        self.clear()
        message = f"Score: {self.score}"
        self.write(message, False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Adjusts the total score number by adding 1 to the total, automatically refreshes message on screen"""
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)
