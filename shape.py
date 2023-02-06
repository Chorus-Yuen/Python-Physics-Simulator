from dataclasses import dataclass

from coord import Coord
from config import *


@dataclass
class Shape:
    disp: Coord
    vel: Coord = Coord(0, 0)
    acc: Coord = Coord(0, -9.8)
    mass: float = 1

    def get_new_disp(self):
        t = RENDERING_RATE
        self.disp += self.vel * t + self.acc * (0.5 * t * t)

        self.vel += self.acc * t


@dataclass
class Circle(Shape):
    radius: float = CIRCLE_RADIUS - CIRCLE_BORDER / 100

    def draw(self, cnv):
        x = self.disp.x * SCALE_FACTOR
        y = WIN_HEIGHT - self.disp.y * SCALE_FACTOR
        rad = self.radius * SCALE_FACTOR
        cir = cnv.create_oval(x - rad, y - rad, x + rad, y + rad,
                              fill=CIRCLE_COLOUR, width=1, outline=CIRCLE_COLOUR)
        return cir

    def not_out_of_screen(self):
        if 1 <= self.disp.x + self.radius and self.disp.x - self.radius <= WIN_WIDTH / SCALE_FACTOR:
            return False
        return True