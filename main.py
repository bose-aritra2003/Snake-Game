# Snake Game

# This is based on the old school snake game we all used to play on keypad phones

import time
from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor("black")

my_snake = Snake()
my_food = Food()
my_score = Scoreboard()

screen.listen()
screen.onkey(my_snake.turnUp, key="Up")
screen.onkey(my_snake.turnDown, key="Down")
screen.onkey(my_snake.turnLeft, key="Left")
screen.onkey(my_snake.turnRight, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # To give that old school feeling
    my_snake.move()
    # screen.update() with tracer set to zero is used to prevent the jittery animation caused
    # due to the forloop moving one my_snake segment at a time rather than moving all at once.
    # So the update() method update the screen only when al the my_snake segments has been moved the desired distance.
    # Note that update() method should only be used with tracer(0) that is off.

    # Detecting collision of snake with food
    if my_snake.head.distance(my_food) < 15:
        # Food is not a point object, it has a dimension of 10 by 10, so we add some buffer that is
        # collision occurs when distance between snake and food is less than 15 pixels
        my_food.resetFood()
        my_snake.extendSnake()
        my_score.updateScore()

    # Detecting collision of snake with wall
    wall_collision = my_snake.head.xcor() > 280 or \
                     my_snake.head.xcor() < -280 or \
                     my_snake.head.ycor() > 280 or \
                     my_snake.head.ycor() < -280
    if wall_collision:
        my_score.reset()
        my_snake.reset()

    # Detect tail collision
    for segment in my_snake.segments[1:]:
        # The above slicing from [1:] is done because the head is also a segment
        if my_snake.head.distance(segment) < 10:
            my_score.reset()
            my_snake.reset()


screen.exitonclick()
