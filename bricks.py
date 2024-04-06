import turtle as t


class Bricks:

    def __init__(self):

        self.bricks = []
        y_cor = 215
        for color in ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3']:
            x_cor = -364
            for _ in range(16):
                new_brick = t.Turtle()
                new_brick.shape('square')
                new_brick.color(color)
                new_brick.shapesize(1.2, 2.4)
                new_brick.hideturtle()
                new_brick.penup()
                new_brick.goto((x_cor, y_cor))
                new_brick.showturtle()
                self.bricks.append(new_brick)
                x_cor += 48
            y_cor -= 24
