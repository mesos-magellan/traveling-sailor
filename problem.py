# -*- coding: utf-8 -*-
# https://github.com/perrygeo/simanneal/blob/master/LICENSE.txt
# https://github.com/perrygeo/simanneal/blob/master/examples/salesman.py

from __future__ import print_function
import math
import random
import os
import codecs
import json
from simanneal import Annealer


def distance(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    R = 3963  # radius of Earth (miles)
    # print("a: {} b: {}".format(a,b))
    try:
        lat1, lon1 = math.radians(a[0]), math.radians(a[1])
        lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    except:
        raise
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

def read(filename):
        """Read and return `filename` in root dir of project and return string"""
        here = os.path.abspath(os.path.dirname(__file__))
        return codecs.open(os.path.join(here, filename), 'r').read()

cities = json.loads(read("cities.json"))