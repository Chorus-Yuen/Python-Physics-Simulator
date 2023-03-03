import time
import tkinter as tk

from config import *
from ground import Ground
from coord import Coord
from shape import Circle
from simulation import Simulation
from display import create_cnv, setup_display
from collision import check_collisions


class Environment:
    def __init__(self, sim_choice):
        self.grounds = []
        self.circles = []
        self.sim_choice = sim_choice
        self.setup()
        self.root = tk.Tk()
        self.cnv = create_cnv(self.root, tk)
        setup_display(self.root, self.cnv, self.grounds, self.circles)
        self.run()
        self.root.mainloop()

    def setup_grounds(self, sim):
        args = sim.select_ground(GROUND_SIM_NUM)
        for arg in args:
            ground = Ground(Coord(arg[0], arg[1]), Coord(arg[2], arg[3]))
            self.grounds.append([ground])

    def setup_circles(self, sim):
        for arg in sim.select_circle(self.sim_choice):
            arg[7] -= CIRCLE_BORDER / 100
            cir = Circle(Coord(arg[0], arg[1]), Coord(arg[2], arg[3]),
                         Coord(arg[4], arg[5]), arg[6], arg[7])
            self.circles.append([cir])

    def setup(self):
        sim = Simulation()
        self.setup_circles(sim)
        self.setup_grounds(sim)

    def update_circle(self, j):
        self.circles[j][0].get_new_disp(len(self.circles))
        old_cir = self.circles[j][1]
        if self.circles[j][0].not_out_of_screen():
            self.circles.pop(j)
        else:
            # self.circles[j][0].angle += 360 / VEL_SCALED
            self.circles[j][1] = self.circles[j][0].draw(self.cnv)
            j += 1
        if old_cir:
            self.cnv.delete(old_cir[0])
            self.cnv.delete(old_cir[1])
        return j

    def run(self):
        i = 0
        while self.circles:
            check_collisions(self.circles, self.grounds)
            #time.sleep(10 ** -32)
            j = 0
            try:
                while j < len(self.circles):
                    j = self.update_circle(j)
                self.root.update()
            except tk.TclError:
                quit()
            i += 1