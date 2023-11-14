from turtle import Screen
from snake import Snake
from dot import Dot
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Snake: The Game')
screen.tracer(0)
snake = Snake()
dot = Dot()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.movement()

    if snake.head.distance(dot) < 15:
        dot.refresh()
        snake.extend()
        scoreboard.add_point()
    elif snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        scoreboard.reset_self()
        snake.reset_snake()

    for segment in snake.snakes[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_self()
            snake.reset_snake()


screen.exitonclick()
