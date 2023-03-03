from random import randint

WIN_WIDTH = 1300
WIN_HEIGHT = 800
BG_COLOUR = "light blue"
CIRCLE_COLOUR_1 = "grey"
CIRCLE_COLOUR_2 = "dark grey"
GROUND_COLOUR = "black"

GROUND_CIRCLE_E = 0.8
CIRCLE_CIRCLE_E = 0.8
COEF_OF_FRICTION = 0.3
IMPACT_DURATION = 1

CIRCLE_RADIUS = 4
CIRCLE_BORDER = 2 # Pixels

RENDERING_RATE = 1 / 100000

SIZE_SCALED = 10
VEL_SCALED = 400 #/ (RENDERING_RATE * 10000)
THRESHOLD_DEPTH = 0.01

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
circles_args_list = [[[30, 60, 5, 0, 0, -9.8, 1, 4],
                      [50, 60, -5, 0, 0, -9.8, 1, 4]],

                     [[66, 55, 0, 2, 0, -9.8, 1, 4],
                      [60, 14, 0, 0, 0, -9.8, 1, 4]],

                     [[20, 32, 7, 2, 0, -9.8, 1, 4],
                      [100, 30, -5, 1, 0, -9.8, 1, 4]],

                     [[20, 32, 7, 2, 0, -9.8, 1, 4],
                      [100, 30, -5, 1, 0, -9.8, 1, 4],
                      [60, 50, 1, -10, 0, -9.8, 1, 4]],

                     [[10 + 130 / 5 * i, 40 + randint(0, 10) * 2, randint(-5, 5),
                       randint(-2, 2), 0, -9.8, 1, 4] for i in range(5)],

                     [[130, 60, 0, 0, 0, -9.8, 1, 4]],

                     [[50, 15, 0, 0, 0, -9.8, 1, 5],
                      [60, 15, 0, 0, 0, -9.8, 1, 5]]]

# 1: two horizontal
# 2: two diagonal
# 3: two bounce to the middle
# 4: three messy
# 5: pick num
# 6: one rolling
# 7: two stationary