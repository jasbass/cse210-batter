import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICKS = [os.path.join(os.getcwd(), "./batter/assets/brick-0.png"), 
os.path.join(os.getcwd(), "./batter/assets/brick-1.png"),
os.path.join(os.getcwd(), "./batter/assets/brick-2.png"),
os.path.join(os.getcwd(), "./batter/assets/brick-3.png"),
os.path.join(os.getcwd(), "./batter/assets/brick-4.png"),
os.path.join(os.getcwd(), "./batter/assets/brick-5.png"),
os.path.join(os.getcwd(), "./batter/assets/brick-6.png")
]
IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")


BALL_WIDTH = 24
BALL_HEIGHT = 24

BALL_X = (MAX_X / 2) - (BALL_WIDTH / 2)
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

PADDLE_X = (MAX_X / 2) - (PADDLE_WIDTH / 2)
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

PADDLE_SPEED = 15


