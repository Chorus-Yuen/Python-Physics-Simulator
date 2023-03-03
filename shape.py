from dataclasses import dataclass
from math import cos, atan, pi

from coord import Coord
from config import *


@dataclass
class Shape:
    disp: Coord
    vel: Coord
    acc: Coord = Coord(0, -9.8)
    mass: float = 1

    def get_new_disp(self, num):
        t = RENDERING_RATE
        vel = self.vel * VEL_SCALED * num
        acc = self.acc * VEL_SCALED * num
        self.disp += vel * t + acc * (0.5 * t * t)
        self.vel += acc * t


@dataclass
class Circle(Shape):
    radius: float = CIRCLE_RADIUS - CIRCLE_BORDER / 100
    theta: float = 0
    omega: float = 0

    def update_spin(self, grad):
        t = RENDERING_RATE
        angle = atan(grad)
        val = self.acc.y * COEF_OF_FRICTION * t * cos(angle) / self.radius * VEL_SCALED
        self.theta += self.omega * t - val * t / 2
        self.theta *= 180 / (2 * pi)
        self.omega -= val

    def draw(self, cnv):
        x = self.disp.x * SIZE_SCALED
        y = WIN_HEIGHT - self.disp.y * SIZE_SCALED
        rad = self.radius * SIZE_SCALED
        upper_chord = cnv.create_arc(x - rad, y - rad, x + rad, y + rad,
                                     start=self.theta + 180, extent=180,
                                     fill=CIRCLE_COLOUR_1, outline=CIRCLE_COLOUR_1)
        lower_chord = cnv.create_arc(x - rad, y - rad, x + rad, y + rad,
                                     start=self.theta, extent=180,
                                     fill=CIRCLE_COLOUR_2, outline=CIRCLE_COLOUR_2)
        return upper_chord, lower_chord

    def not_out_of_screen(self):
        if 1 <= self.disp.x + self.radius and self.disp.x - self.radius <= WIN_WIDTH / SIZE_SCALED:
            return False
        return True