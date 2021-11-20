from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    def __init__(self):
        pass

    def execute(self, cast):
        self._move_paddles(cast)
        self._move_balls(cast)

    def _move_paddles(self, cast):
        for paddle in cast['paddle']:
            position = paddle.get_position()
            x = position.get_x()
            y = position.get_y()
            velocity = paddle.get_velocity()
            dx = velocity.get_x()
            dy = velocity.get_y()
            x += dx
            y += dy
            paddle.set_position(Point(x, y))

    def _move_balls(self, cast):
        for ball in cast['balls']:
            position = ball.get_position()
            x = position.get_x()
            y = position.get_y()
            velocity = ball.get_velocity()
            dx = velocity.get_x()
            dy = velocity.get_y()
            x += dx
            y += dy
            ball.set_position(Point(x, y))


