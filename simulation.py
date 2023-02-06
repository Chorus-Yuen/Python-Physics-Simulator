from config import circles_args_list, grounds_args_list

class Simulation:
    def __init__(self):
        self.ground_args = grounds_args_list
        self.circle_args = circles_args_list

    def select_ground(self, ind):
        if ind <= len(self.ground_args):
            return self.ground_args[ind - 1]
        elif len(self.ground_args) >= 0:
            return self.ground_args[0]
        else:
            return []

    def select_circle(self, ind):
        if ind <= len(self.circle_args):
            return self.circle_args[ind - 1]
        elif len(self.circle_args) >= 0:
            return self.circle_args[0]
        else:
            return []