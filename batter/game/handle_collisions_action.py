from game import constants
from game.action import Action
import random
from game.ball import Ball
from game.point import Point

class HandleCollisionsAction(Action):
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        self._check_paddle_collisions(cast)
        self._check_brick_collisions(cast)

    def _check_paddle_collisions(self, cast):
        for ball in cast['balls']:
            for paddle in cast['paddle']:
                if self._physics_service.is_collision(ball, paddle):
                    horizontal_bounce_area = 0.10 * paddle.get_width()
                    right_edge = paddle.get_right_edge()
                    left_edge = paddle.get_left_edge()
                    if ((right_edge - horizontal_bounce_area) <= ball.get_left_edge() <= right_edge) or ((left_edge - horizontal_bounce_area) >= ball.get_right_edge() >= left_edge):
                        ball.bounce_horizontal()
                    ball.bounce_vertical()
                    self._audio_service.play_sound(constants.SOUND_BOUNCE)

    def _check_brick_collisions(self, cast):
        for ball in cast['balls']:
            for brick in cast['bricks']:
                if self._physics_service.is_collision(ball, brick):
                    horizontal_bounce_area = 0.10 * brick.get_width()
                    right_edge = brick.get_right_edge()
                    left_edge = brick.get_left_edge()
                    if ((right_edge - horizontal_bounce_area) <= ball.get_left_edge() <= right_edge) or ((left_edge + horizontal_bounce_area) >= ball.get_right_edge() >= left_edge):
                        ball.bounce_horizontal()
                    vertical_bounce_area = 0.30 * brick.get_height()
                    top_edge = brick.get_top_edge()
                    bottom_edge = brick.get_bottom_edge()
                    if ((bottom_edge - vertical_bounce_area) <= ball.get_top_edge() <= bottom_edge) or ((top_edge + vertical_bounce_area) >= ball.get_bottom_edge() >= top_edge):
                        ball.bounce_vertical()
                    cast['bricks'].remove(brick)
                    chance = random.randint(1,10)
                    if chance == 1:
                        self._spawn_new_ball(cast)
                    self._audio_service.play_sound(constants.SOUND_BOUNCE)

    def _spawn_new_ball(self, cast):
        ball = Ball()
        ball.set_position(Point(constants.BALL_X, constants.BALL_Y))
        ball.set_velocity(Point(constants.BALL_DX, constants.BALL_DY))
        cast['balls'].append(ball)

                    