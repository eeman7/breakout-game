import turtle as t


class Paddle(t.Turtle):

    def __init__(self):

        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(0.2, 4)
        self.hideturtle()
        self.penup()
        self.goto((0, -250))
        self.showturtle()
        self.move = 20

    def move_right(self):
        if self.xcor() < 360:
            self.goto(self.xcor() + self.move, self.ycor())

    def move_left(self):
        if self.xcor() > -360:
            self.goto(self.xcor() - self.move, self.ycor())
