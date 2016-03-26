# -*- coding: utf-8 -*-
import os
import json
import codecs
import string


def read(filename):
        """Read and return `filename` in root dir of project and return string"""
        here = os.path.abspath(os.path.dirname(__file__))
        return codecs.open(os.path.join(here, filename), 'r').read()

rawCities = read("cities.txt")

parsedCities = {filter(lambda x: x in string.printable, l.split(",")[2]): tuple(map(float, l.split(",")[-2:]))
                for l in rawCities.strip().splitlines()}

#print("parsed cities is {}".format(parsedCities))

f = open('parsedCities2.json', 'w')
print("json dumps: {}".format(json.dumps(parsedCities)))
json.dump(parsedCities,f)
