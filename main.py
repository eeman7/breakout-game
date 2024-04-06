import turtle as t
import time
from paddle import Paddle
from ball import Ball
from bricks import Bricks

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=780, height=610)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = Bricks()

speed = 0.1

screen.listen()

screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

while len(bricks.bricks) != 0:
    screen.update()
    time.sleep(speed)
    ball.move()
    if ball.xcor() == 384 or ball.xcor() == -384:
        ball.bounce_off_side()
    if ball.ycor() >= 299:
        ball.bounce_off_top()
    if ball.ycor() == -241 and ball.distance(paddle) <= (1649 ** 0.5):
        ball.bounce_off_paddle(paddle)
    for brick in bricks.bricks:
        x_dis = abs(brick.xcor() - ball.xcor())
        y_dis = abs(brick.ycor() - ball.ycor())
        if x_dis <= 18 and y_dis <= 18:
            ball.bounce_off_brick(x_dis, y_dis)
            brick.hideturtle()
            bricks.bricks.remove(brick)

screen.exitonclick()
