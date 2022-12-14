from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBord import ScoreBord

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBord = ScoreBord()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_extend()
        scoreBord.scoreUpdate()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreBord.game_over()

    for seg in snake.segment[1:]:

        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreBord.game_over()

screen.exitonclick()
