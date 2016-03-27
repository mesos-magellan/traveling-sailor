#!/usr/bin/env python

import itertools
import time

from problem import Problem


def bruteforce_tsp(announce_every=500000):
    cities = {
        'Holmesville': (31.7036111, -82.3208333),
        'Jatipasir': (-8.2509, 113.9975),
        'Tapalinna': (-2.923, 119.1626),
        'Sahout el Ma': (16.9166667, -15.1666667),
        'Isanganaka': (-0.683333, 24.083333),
        'El Yerbanis': (29.45, -108.6),
        'Gun-ob': (9.6289, 124.0517),
        'Chak Seventy-five ML': (31.345362, 71.123454),
        'Bakous': (13.7363889, -16.6080556),
        'Metkow Maly': (50.05, 19.4)
    }
    problem_data = dict(
        cities=cities,
        start_city="Bakous",
        updates_enabled=True
    )

    start = time.time()
    t = Problem(cities.keys(), **problem_data)
    fittest = [t.state, t.energy()]
    announce_count = 0
    for state in itertools.permutations(t.cities.keys()):
        announce_count += 1
        t.state = state
        energy = t.energy()
        if energy < fittest[1]:
            fittest = [state, energy]
        if announce_count:
            if announce_count == announce_every:
                print(fittest[1])
                announce_count = 0
    print("Best fitness: {}".format(fittest[1]))
    print("Took {:.2f}s".format(time.time() - start))
    return fittest[1]


def main():
    bruteforce_tsp()


if __name__ == '__main__':
    main()
