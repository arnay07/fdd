# -*- coding: utf-8 -*-

import math

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


def distance(sl1, sl2, sw1, sw2, pl1, pl2, pw1, pw2):
    return math.sqrt(((sl1-sl2)/(maxes['sl']-mins['sl']))**2 + ((sw1-sw2)/(maxes['sw']-mins['sw']))**2 + ((pl1-pl2)/(maxes['pl']-mins['pl']))**2 + ((pw1-pw2)/(maxes['pw']-mins['pw']))**2)


def distance2(sl1, sl2, sw1, sw2, pl1, pl2, pw1, pw2, c1, c2, d1, d2):
    c = 0 if c1 == c2 else 1
    d = 0 if d1 == d2 else 1
    return math.sqrt(((sl1-sl2)/(maxes['sl']-mins['sl']))**2 + ((sw1-sw2)/(maxes['sw']-mins['sw']))**2 + ((pl1-pl2)/(maxes['pl']-mins['pl']))**2 + ((pw1-pw2)/(maxes['pw']-mins['pw']))**2 + c**2 + d**2)


if __name__ == '__main__':
    print("distance(iris1, iris2) is {}".format(
        distance(5.1, 7.0, 3.5, 3.2, 1.4, 4.7, 0.2, 1.4)
    ))

    print("distance(iris1, iris3) is {}".format(
        distance(5.1, 6.3, 3.5, 3.3, 1.4, 6.0, 0.2, 2.5)
    ))

    print("distance(iris2, iris3) is {}".format(
        distance(7.0, 6.3, 3.2, 3.3, 4.7, 6.0, 1.4, 2.5)
    ))

    print("distance2(iris4, iris5) is {}".format(
        distance2(5.6, 4.8, 2.5, 3.4, 3.9, 1.6, 1.1, 0.2,
                  "violet", "jaune", "bulbe", "rhizome")
    ))

    print("distance2(iris4, iris6) is {}".format(
        distance2(5.6, 6.0, 2.5, 3.0, 3.9, 4.8, 1.1, 1.8,
                  'violet', 'jaune', 'bulbe', 'bulbe')
    ))

    print("distance2(iris5, iris6) is {}".format(
        distance2(4.8, 6.0, 3.4, 3.0, 1.6, 4.8, 0.2, 1.8,
                  'jaune', 'jaune', 'rhizome', 'bulbe')
    ))
