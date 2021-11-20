from game.action import Action
from game import constants
from game.point import Point

class HandleOffScreenAction(Action):
    def __init__(self):
        pass

    def execute(self, cast):
        self._check_balls(cast)
        self._check_paddle(cast)

    def _check_balls(self, cast):
        for ball in cast['balls']:
            position = ball.get_position()
            x = position.get_x()
            y = position.get_y()
            width = ball.get_width()
            height = ball.get_height()
            if x < 0 or ((x + width) > constants.MAX_X):
                ball.bounce_horizontal()
            if y < 0:
                ball.bounce_vertical()
            if ((y + height) > constants.MAX_Y):
                cast['balls'].remove(ball)

    def _check_paddle(self, cast):
        for paddle in cast['paddle']:
            position = paddle.get_position()
            x = position.get_x()
            y = position.get_y()
            width = paddle.get_width()
            height = paddle.get_height()
            if x < 0:
                paddle.set_position(Point(0, y))
            if ((x + width) > constants.MAX_X):
                paddle.set_position(Point((constants.MAX_X - width), y))
            if y < 0:
                paddle.set_position(Point(x, 0))
            if ((y + height) > constants.MAX_Y):
                paddle.set_position(Point(x, (constants.MAX_Y - height)))


