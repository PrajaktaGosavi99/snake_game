from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')
SMALL_FONT = ('Arial', 11, 'normal')


class ScoreCard(Turtle):
    """Shows the score at the top of the screen and the game over message."""

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.refresh()

    def refresh(self):
        """Redraw the score at the top."""
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.refresh()

    def reset(self):
        self.score = 0
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write("Press SPACE to restart or ESC to quit", align=ALIGNMENT, font=SMALL_FONT)
