from turtle import Turtle
INITIAL_BODY_COORDINATES = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        """
        Creates the body of the snake and puts it at the center
        """
        for position in INITIAL_BODY_COORDINATES:
            self.addSegment(position)

    def reset(self):
        """
        To delete the old snake and create a new snake
        """
        for seg in self.segments:
            seg.hideturtle()
        self.__init__()

    def addSegment(self, position):
        """
        Takes position of new segment to be added
        """
        new_seg = Turtle("circle")
        new_seg.color("yellow")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extendSnake(self):
        """
        Increase the length of snake by appending a circle turtle at the end of the existing snake
        """
        self.addSegment(self.segments[-1].position())

    def move(self):
        """
        Starts moving the snake forward
        """
        # Below loop is to move the snake so that segments don't detach when any piece moves
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turnUp(self):
        """
        Turns the snake towards north
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turnDown(self):
        """
        Turns the snake towards south
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turnLeft(self):
        """
        Turns the snake towards west
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turnRight(self):
        """
        Turns the snake towards east
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
