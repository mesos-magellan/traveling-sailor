# -*- coding: utf-8 -*-

import itertools
from copy import deepcopy
import time
import json
import os
import codecs

def bruteforce(problem, cities):
    # print("city list length is: {}".format(len(cities)))
    # print("cities is: {}".format(cities))
    tempCities = deepcopy(cities)
    staticItem = tempCities.popitem()
    # print("staticItem is {}".format(staticItem))
    # print("tempCity length is: {}".format(len(tempCities)))
    # print("tempCity is: {}".format(tempCities))

    best_distance = 10000000
    best_key = None

    # print("tempCities length is: {}".format(len(tempCities)))
    # print("city keys are: {}".format(cities.keys()))
    allPermutations = itertools.permutations(tempCities.keys())
    for i in allPermutations:
        newtup = i + (staticItem[0],)
        fitness = problem.energy(newtup)
        if(fitness < best_distance):
            best_distance = fitness
            best_key = newtup

        # print "option {}".format(newtup)
    return best_distance, best_key


def test_answer():
    import sys
    sys.path.append("/home/vagrant/traveling-sailor")
    sys.path.append("../traveling-sailor")
    import problem

    def read(filename):
        """Read and return `filename` in root dir of project and return string"""
        here = os.path.abspath(os.path.dirname(__file__))
        return codecs.open(os.path.join(here, filename), 'r').read()

    cities = json.loads(read("cities.json"))

    # print("{}".format(cities))
    # exit()

    tsp = problem.Problem(cities, None)
    # brute_start = int(round(time.time() * 1000))
    # best_distance, best_solution = bruteforce(tsp,cities)
    # brute_end = int(round(time.time() * 1000))
    # print("best solution is {} with key {}".format(best_distance,best_solution))
    # print("brute took: {}".format(brute_end - brute_start))

    anneal_start = int(round(time.time() * 1000))
    tsp.copy_strategy = "slice"
    auto_schedule = tsp.auto(minutes=5)
    tsp.set_schedule(auto_schedule)
    good_solution, good_distance = tsp.anneal()
    anneal_end = int(round(time.time() * 1000))

    print("good solution took is {} with key {}".format(good_distance,good_solution))

    print("anneal took: {}".format(anneal_end - anneal_start))

    # print("good solution is {} with key {}".format(good_distance,good_solution))
    # assert anneal(1000,0.2,cities.keys(),50000,problem) == 0
    # assert best_solution >= good_solution
    # assert (anneal_end - anneal_start) < (brute_end - brute_start)


if __name__ == "__main__":
    test_answer()
