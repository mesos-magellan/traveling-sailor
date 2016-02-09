# -*- coding: utf-8 -*-
# https://github.com/perrygeo/simanneal/blob/master/LICENSE.txt
# https://github.com/perrygeo/simanneal/blob/master/examples/salesman.py

from __future__ import print_function
import math
import random
from simanneal import Annealer


def distance(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    R = 3963  # radius of Earth (miles)
    # print("a: {} b: {}".format(a,b))
    try:
        lat1, lon1 = math.radians(a[0]), math.radians(a[1])
        lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    except:
        print("a: {} b: {}".format(a,b))
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

cities.update({" ".join(l.split()[:-2]): tuple(map(float, l.split()[-2:])) for l in ("""
Hasanabad-e Abdar	34.273695	48.443265
Inikchievo	42.2166667	25.75
Faëndou	9.0166667	-10.2
Eiliboshoek	51.1	4.466667
Shuangshugangzi	41.413628	122.74929
Kiniangi	-5.1833333	16.6166667
Chak Forty-Twelve L	30.508333	72.688889
Vurgash	34.7175	67.843889
Jawalanukhi	31.883333	76.316667
Staversvad	56.2	14.316667
Ray	55.0352778	-7.7216667
The Oaks	37.8938889	-75.5111111
Shunyah	34.053056	68.293611
Al Tawilah	20.2487	41.361693
El Paye	20.1	-99.575
Trapeang Kraleng	11.3833333	104.3833333
Dhoriaí	35.2833333	25.6666667
Lemasan	-7.0287	112.8359
Dos Latarice	19.1333333	-72.2
Kampung Pedas Tengah	2.6051	102.0489
Djuraganan	-6.216667	106.783333
Mefalso	14.8155556	38.8383333
Real	40.448454	-8.13759
Hawley	42.7341667	-113.395
Gari	55.869236	52.026078
Sahalava	-23.1166667	46.1666667
Voshazhnikovo	57.361565	39.139824
Dara Miana	35.635	45.8136111
Zangaka	34.8791667	45.4125
Verkhnya Lukovytsya	49.145531	23.778323
Zerong	24.883333	104.975
Järvenperä	60.616667	21.55
Goth Hot Brahmani	26.571429	67.481906
Kalab-e Sofla	28.5731	57.7189
Na Phèo	22.083333	106.7
Driestenbroek	50.783333	3.766667
Ban Sao Rong Hie	14.564444	100.195278
Fiinka	3.5833333	43.8166667
Ban Khlong Thap Chong Bon	13.740722	100.699889
Monastírion	37.2333333	21.8166667
Alcúlar	36.966939	-3.192399
Zabely	-21.9666667	43.6333333
Mograr Foukania	32.5166667	-0.5833333
Ta Wai	16.25	107
Rawal Kot	34.788503	73.513134
Tiénza	-4.02	11.6358333
Grytski	53.0166667	24.1
Wahali Zer	32.756004	73.042559
Babani	-12.3	43.8
Sabanatha	23.1666667	95.7166667
Taksyrovo	53.2352	58.6545
Avsar	37.579722	27.425
Çerçiler	41.152357	32.613582
Hagen	58.9	6.083333
Zuthem	52.459679	6.171785
Bialoboki	50.024767	22.389329
Skudayen	53.268185	20.405694
Boyanangele	3.45	20.5
Nbara Akuma	5.470704	7.443424
Bekurejo	-7.62	110.573611
Gândara	41.703283	-8.70761
El Duraznillo	21.7875	-102.165278
Pagadengan	-3.4024	120.1483
Guselshchikov	47.160342	38.082837
Binsakou	10.9980556	3.1488889
Bukyanju	-0.6333333	31.7666667
Sherdil	34.275226	71.867837
Vegerbol	59.466667	12.883333
Neyakan	32.559318	50.134823
Kolluca	38.733333	39.616667
Jinjbiniali	26.216667	70.8
Bu Ali	34.701809	11.19616
Carkhak	35.865484	66.834027
Shangshengting	23.820833	106.309444
Ban Lakhum-Nua	16.5575	106.418056
Letimbou	34.8583333	32.5166667
Akuse	7.083333	8.8
Nenorova	57.391846	41.105841
Dourouba	7.9469444	-8.5708333
Roodekop	-27.563056	29.987731
Dahane Yakhsi	34.006111	68.038611
Brîssât	34.2333333	35.95
Lilla Fagraryd	57.35	15.116667
Antônio Bastos	-29.983333	-56.883333
Khadzhi-Alam-Kala	32.947953	68.665587
Dalangan 2	-7.373611	110.454167
Wachangcun	28.325059	104.68882
Tanque del Grullo	24.066667	-102.383333
Atu	31.210456	66.381669
Vinatori	46.9	26.4
Urrutia Hacienda	-13.6833333	-76.0666667
Loveren	51.45	4.916667
Kedungbalar Kidul	-7.895278	110.941389
Le Crouzet	44.177432	3.474414
Buôn Dur Mah	12.316667	108.216667
Bi'r ash Shu`li	15.2352778	42.8486111
Erakovice	43.270556	19.648333
Kupche	49.98125	24.558444
Youfangping	33.6	106.566667
Pedregal	-1.2833333	-79.7833333
""").strip().splitlines()})
