from game.action import Action
from game.point import Point
from game import constants

class ControlActorsAction(Action):
    def __init__(self, input_service):
        self._input_service = input_service

    def execute(self, cast):
        direction = self._input_service.get_direction()
        x = direction.get_x()
        y = direction.get_y()
        dx = constants.PADDLE_SPEED * x
        dy = constants.PADDLE_SPEED * y
        for paddle in cast['paddle']:
            paddle.set_velocity(Point(dx, dy))

            
