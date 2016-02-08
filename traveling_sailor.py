# https://github.com/perrygeo/simanneal/blob/master/LICENSE.txt
# https://github.com/perrygeo/simanneal/blob/master/examples/salesman.py

import math
import random
from abc import ABCMeta, abstractmethod


class Problem(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.init()

    @abstractmethod
    def init(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def fitness_score(self, key):
        raise NotImplementedError

    @abstractmethod
    def mutation(self, key):
        raise NotImplementedError


class TSPSA(Problem):
    def init(self, cities):
        self.cities = cities

         # initial state, a randomly-ordered itinerary
        init_state = list(cities.keys())
        random.shuffle(init_state)

        # create a distance matrix
        self.distance_matrix = {}
        for ka, va in cities.items():
            self.distance_matrix[ka] = {}
            for kb, vb in cities.items():
                if kb == ka:
                    self.distance_matrix[ka][kb] = 0.0
                else:
                    self.distance_matrix[ka][kb] = self.distance(va, vb)

    @staticmethod
    def distance(a, b):
        """Calculates distance between two latitude-longitude coordinates."""
        R = 3963  # radius of Earth (miles)
        lat1, lon1 = math.radians(a[0]), math.radians(a[1])
        lat2, lon2 = math.radians(b[0]), math.radians(b[1])
        return math.acos(math.sin(lat1) * math.sin(lat2) +
                         math.cos(lat1) * math.cos(lat2) *
                         math.cos(lon1 - lon2)) * R

    def mutation(self, state):
        """Swaps two cities in the route."""
        a = random.randint(0, len(state) - 1)
        b = random.randint(0, len(state) - 1)
        state[a], state[b] = state[b], state[a]
        return state

    def energy(self, state):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(state)):
            e += self.distance_matrix[state[i-1]][state[i]]
        return e
