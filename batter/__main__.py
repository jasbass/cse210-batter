import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.ball import Ball
from game.paddle import Paddle
from game.draw_actors_action import DrawActorsAction
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.brick import Brick


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    for row in range(14):
        x = 30 + ((constants.BRICK_WIDTH + 5) * row)
        for column in range(7):
            brick = Brick()
            y = 30 + ((constants.BRICK_HEIGHT + 5) * column)
            brick.set_position(Point(x,y))
            brick.set_image(constants.IMAGE_BRICKS[column])

            cast['bricks'].append(brick)

    cast["balls"] = []
    ball = Ball()
    ball.set_position(Point(constants.BALL_X, constants.BALL_Y))
    ball.set_velocity(Point(constants.BALL_DX, constants.BALL_DY))
    cast['balls'].append(ball)

    cast["paddle"] = []
    paddle = Paddle()
    paddle.set_position(Point(constants.PADDLE_X, constants.PADDLE_Y))
    cast['paddle'].append(paddle)
    
    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service)
    handle_off_screen_action = HandleOffScreenAction()

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [handle_off_screen_action, handle_collisions_action, move_actors_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
