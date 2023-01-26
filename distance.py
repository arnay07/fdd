# -*- coding: utf-8 -*-

import math


def distance(sl1, sl2, sw1, sw2, pl1, pl2, pw1, pw2):
    maxes = {
        'sl': 7.9,
        'sw': 4.4,
        'pl': 6.9,
        'pw': 2.5
    }
    mins = {
        'sl': 4.3,
        'sw': 2.0,
        'pl': 1.0,
        'pw': 0.1
    }
    return math.sqrt(((sl1-sl2)/(maxes['sl']-mins['sl']))**2 + ((sw1-sw2)/(maxes['sw']-mins['sw']))**2 + ((pl1-pl2)/(maxes['pl']-mins['pl']))**2 + ((pw1-pw2)/(maxes['pw']-mins['pw']))**2)


if __name__ == '__main__':
    print("distance(iris1, iris2) is {}".format(
        distance(5.1, 7.0, 3.5, 3.2, 1.4, 4.7, 0.2, 1.4)))

    print("distance(iris1, iris3) is {}".format(
        distance(5.1, 6.3, 3.5, 3.3, 1.4, 6.0, 0.2, 2.5)))

    print("distance(iris2, iris3) is {}".format(
        distance(7.0, 6.3, 3.2, 3.3, 4.7, 6.0, 1.4, 2.5)))
