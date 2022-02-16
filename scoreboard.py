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

        # read high score from file
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.update_score()

    def update_score(self):
        """Renders the score message on screen"""
        self.clear()
        message_score = f"Score: {self.score}"
        message_high_score = f"High Score: {self.high_score}"
        self.write(message_score + " " + message_high_score, False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Adjusts the total score number by adding 1 to the total, automatically refreshes message on screen"""
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

            # save the high score by writing to an external file
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_score()
