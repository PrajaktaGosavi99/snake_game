import time
from tkinter import TclError
from turtle import Screen, Terminator

from snake import Snake
from food import Food
from score import ScoreCard

WALL_DISTANCE = 300 - 20
FRAME_DELAY = 0.1


class Game:
    """Ties the snake, food and scoreboard together and runs the game loop."""

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.scorecard = ScoreCard()

        self.running = True
        self.is_over = False
        self.bind_keys()

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.restart, "space")
        self.screen.onkey(self.quit, "Escape")

    def hit_wall(self):
        head = self.snake.head
        return (abs(head.xcor()) > WALL_DISTANCE
                or abs(head.ycor()) > WALL_DISTANCE)

    def end_game(self):
        self.is_over = True
        self.scorecard.game_over()

    def restart(self):
        """Start a new round, but only if the current one has ended."""
        if not self.is_over:
            return
        self.snake.reset()
        self.scorecard.reset()
        self.food.refresh()
        self.is_over = False

    def quit(self):
        self.running = False

    def run(self):
        try:
            while self.running:
                self.screen.update()
                time.sleep(FRAME_DELAY)

                if self.is_over:
                    continue

                self.snake.move()

                if self.snake.head.distance(self.food) < 20:
                    self.food.refresh()
                    self.scorecard.update_score()
                    self.snake.append_segments()

                if self.hit_wall() or self.snake.detect_tail_collision():
                    self.end_game()
            self.screen.bye()
        except (Terminator, TclError):
            # The window was closed with the X button
            pass


if __name__ == "__main__":
    Game().run()
