from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """The snake: a list of square turtle segments, where the first one is the head."""

    def __init__(self):
        self.segments = []
        self.head = None
        self.create_segments()

    def create_segments(self):
        """Build the starting snake and set its head."""
        for position in STARTING_POSITIONS:
            self.add_segments(position)
        self.head = self.segments[0]

    def add_segments(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        new_segment.speed('slowest')
        self.segments.append(new_segment)

    def append_segments(self):
        """Grow the snake by one segment at the tail."""
        self.add_segments(self.segments[-1].position())

    def reset(self):
        """Throw away the old snake and start fresh (used when restarting)."""
        for segment in self.segments:
            segment.goto(1000, 1000)  # move off screen
            segment.hideturtle()
        self.segments.clear()
        self.create_segments()

    def move(self):
        """Each segment moves into the spot of the one in front; the head steps forward."""
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def detect_tail_collision(self):
        """True if the head touches any other segment."""
        return any(self.head.distance(segment) < 10 for segment in self.segments[1:])
