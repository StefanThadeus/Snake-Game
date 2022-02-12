from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=position[0], y=position[1])
        self.snake_segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the snake"""
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            # set snake head towards 90 degrees (go up)
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            # set snake head towards 270 degrees (go down)
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            # set snake head towards 180 degrees (go left)
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            # set snake head towards 0 degrees (go right)
            self.head.setheading(RIGHT)
