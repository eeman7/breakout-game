import turtle as t


class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.6, 0.6)
        self.hideturtle()
        self.penup()
        self.goto((0, -241))
        self.showturtle()
        self.x_move = 12
        self.y_move = 12

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_off_side(self):
        self.x_move *= -1

    def bounce_off_brick(self, x_dis, y_dis):
        self.y_move *= -1

    def bounce_off_paddle(self, paddle):
        self.y_move *= -1
        if ((self.xcor() - paddle.xcor()) > 30 and self.x_move < 0)\
                or ((self.xcor() - paddle.xcor()) < -30 and self.x_move > 0):
            self.x_move *= -1

    def bounce_off_top(self):
        self.y_move *= -1
