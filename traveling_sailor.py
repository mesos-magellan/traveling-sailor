# https://github.com/perrygeo/simanneal/blob/master/LICENSE.txt
# https://github.com/perrygeo/simanneal/blob/master/examples/salesman.py

from __future__ import print_function
import math
import random
from simanneal import Annealer


def distance(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    R = 3963  # radius of Earth (miles)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R


class TSPSA(Annealer):

    """Test annealer with a travelling salesman problem.
    """

    # pass extra data (the distance matrix) into the constructor
    def __init__(self, cities, state=None):
        self.cities = cities

        # create a distance matrix
        self.distance_matrix = {}
        for ka, va in cities.items():
            self.distance_matrix[ka] = {}
            for kb, vb in cities.items():
                if kb == ka:
                    self.distance_matrix[ka][kb] = 0.0
                else:
                    self.distance_matrix[ka][kb] = distance(va, vb)

            # initial state, a randomly-ordered itinerary
        state = list(cities.keys())
        random.shuffle(state)

        super(TSPSA, self).__init__(state)  # important!

    def move(self, state=None):
        """Swaps two cities in the route."""
        state = self.state if state is None else state
        if state == "" or state is None:
             # initial state, a randomly-ordered itinerary
            state = self.cities.keys()
            random.shuffle(state)
        a = random.randint(0, len(state) - 1)
        b = random.randint(0, len(state) - 1)
        state[a], state[b] = state[b], state[a]

    def energy(self, state=None):
        """Calculates the length of the route."""
        state = self.state if state is None else state
        e = 0
        for i in range(len(state)):
            e += self.distance_matrix[state[i-1]][state[i]]
        return e
