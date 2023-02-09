
import numpy as np
from random import randint


class DistanceCalculator():
    def __init__(self):
        self.coord_arr = [[0, 0, 0], [0, 0, 0], [
            0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def get_speed(self, x, y, z):
        self.add_to_queue(x, y, z)
        delta_dist = self.calc_distance()
        # (1/fps) * frames between distance measures = 0.25
        delta_dist = delta_dist / 0.25

        return delta_dist

    # Calculates the distance between first and last cordinates in cordinate array

    def calc_distance(self):
        dx = self.coord_arr[5][0]-self.coord_arr[0][0]
        dy = self.coord_arr[5][1]-self.coord_arr[0][1]
        dz = self.coord_arr[5][2]-self.coord_arr[0][2]
        d = np.sqrt(((dx)**2 + (dy)**2 + (dz)**2)) / 1000

        return d

    # Moves every item in the list by one ans add new cordinates (x, y, z) to the beginning of the list.
    def add_to_queue(self, x, y, z):
        for q in range(1, 6):
            self.coord_arr.insert(6-q, self.coord_arr.pop(5-q))

        self.coord_arr[0][0] = x
        self.coord_arr[0][1] = y
        self.coord_arr[0][2] = z
