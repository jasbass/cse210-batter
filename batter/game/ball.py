from game.actor import Actor
from game import constants
from game.point import Point

class Ball(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(constants.BALL_HEIGHT)
        self.set_width(constants.BALL_WIDTH)
        self.set_image(constants.IMAGE_BALL)

    def bounce_horizontal(self):
        velocity = self.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()
        dx *= -1
        self.set_velocity(Point(dx, dy))

    def bounce_vertical(self):
        velocity = self.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()
        dy *= -1
        self.set_velocity(Point(dx, dy))

    def bounce_up(self):
        velocity = self.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y()
        self.set_velocity(Point(dx, abs(dy)))

