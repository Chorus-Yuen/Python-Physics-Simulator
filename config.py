from random import randint

WIN_WIDTH = 1300
WIN_HEIGHT = 800
SCALE_FACTOR = 10
BG_COLOUR = "light blue"
CIRCLE_COLOUR = "dark grey"
GROUND_COLOUR = "black"

NUM_OF_FRAMES = 200
THRESHOLD_DEPTH = 0.01

GROUND_CIRCLE_E = 0.7
CIRCLE_CIRCLE_E = 0.7

CIRCLE_RADIUS = 4
CIRCLE_BORDER = 2 # Pixels

RENDERING_RATE = 0.098

GROUND_SIM_NUM = 2
CIRCLE_SIM_NUM = 5

# [x1, y1, x2, y2]
grounds_args_list = [[[0, 10, WIN_WIDTH, 10]],

                     [[0, 10, 600, 10],
                      [600, 10, WIN_WIDTH, 25]],

                     [[0, 15, WIN_WIDTH/3, 10],
                      [WIN_WIDTH/3, 10, WIN_WIDTH*2/3, 10],
                      [WIN_WIDTH*2/3, 10, WIN_WIDTH, 15]]]

# [sx, sy, vx, vy, ax, ay, m, r]
circles_args_list = [[[40, 60, 4, 0, 0, -9.8, 1, 4],
                      [60, 60, -4, 0, 0, -9.8, 1, 4]],

                     [[40, 42, 4, 2, 0, -9.8, 1, 4],
                      [60, 40, -5, 0, 0, -9.8, 1, 4]],

                     [[20, 32, 7, 2, 0, -9.8, 1, 4],
                      [100, 30, -5, 1, 0, -9.8, 1, 4]],

                     [[20, 32, 7, 2, 0, -9.8, 1, 4],
                      [100, 30, -5, 1, 0, -9.8, 1, 4],
                      [60, 50, 1, -10, 0, -9.8, 1, 4]],

                     [[i * 10, 40 + randint(0, 10) * 2, randint(-5, 5),
                       randint(-1, 1), 0, -9.8, 1, randint(2, 3)] for i in range(20)],

                     [[0, 14, 5, 0, 0, -9.8, 1, 4]]]

# 1: two horizontal
# 2: two diagonal
# 3: two bounce to the middle
# 4: three messy
# 5: pick num
# 6: one rolling