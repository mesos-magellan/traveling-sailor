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


class Problem(Annealer):
    """Traveling Salesman Problem Annealer

    :param dict job_data: Unused currently
    :param list state: state of the current annealer process
    """
    def __init__(self, job_data, state):
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

        super(Problem, self).__init__(state)  # important!
        self.copy_strategy = "slice"

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


# XXX We are packaging the data with the task for the moment
# latitude and longitude for the twenty largest U.S. cities
cities = {
    'New York City': (40.72, 74.00),
    'Los Angeles': (34.05, 118.25),
    'Chicago': (41.88, 87.63),
    'Houston': (29.77, 95.38),
    'Phoenix': (33.45, 112.07),
    'Philadelphia': (39.95, 75.17),
    'San Antonio': (29.53, 98.47),
    'Dallas': (32.78, 96.80),
    'San Diego': (32.78, 117.15),
    'San Jose': (37.30, 121.87),
    'Detroit': (42.33, 83.05),
    'San Francisco': (37.78, 122.42),
    'Jacksonville': (30.32, 81.70),
    'Indianapolis': (39.78, 86.15),
    'Austin': (30.27, 97.77),
    'Columbus': (39.98, 82.98),
    'Fort Worth': (32.75, 97.33),
    'Charlotte': (35.23, 80.85),
    'Memphis': (35.12, 89.97),
    'Baltimore': (39.28, 76.62)
}
