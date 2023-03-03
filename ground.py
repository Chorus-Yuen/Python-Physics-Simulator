from dataclasses import dataclass

from config import WIN_HEIGHT, SIZE_SCALED, GROUND_COLOUR
from coord import Coord

@dataclass
class Ground:
    coord_a: Coord
    coord_b: Coord

    def draw(self, cnv):
        y1 = WIN_HEIGHT - self.coord_a.y * SIZE_SCALED
        y2 = WIN_HEIGHT - self.coord_b.y * SIZE_SCALED
        return cnv.create_polygon(self.coord_a.x, WIN_HEIGHT, self.coord_a.x, y1,
                                  self.coord_b.x, y2, self.coord_b.x, WIN_HEIGHT,
                                  fill=GROUND_COLOUR, width=0)

    def get_direction_vec(self):
        return Coord((self.coord_b.x - self.coord_a.x) / 10, self.coord_b.y - self.coord_a.y)
