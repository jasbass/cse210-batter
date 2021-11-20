from game.actor import Actor
from game import constants

class Paddle(Actor):
    def __init__(self):
        super().__init__()
        self.set_height(constants.PADDLE_HEIGHT)
        self.set_width(constants.PADDLE_WIDTH)
        self.set_image(constants.IMAGE_PADDLE)
        