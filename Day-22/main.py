from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBord import ScoreBord

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
scoreBord = ScoreBord()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.ycor() > -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreBord.left_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreBord.right_point()

screen.exitonclick()
