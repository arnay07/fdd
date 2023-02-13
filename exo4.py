import math

maxes = {
    'nbEsp': 11,
    'nbBases': 4,
    'diametre': 120536
}

mins = {
    'nbEsp': 0,
    'nbBases': 0,
    'diametre': 2300
}

"""
définition de la formule

d(p1, p2) = sqrt((nbEsp1-nbEsp2)/(maxes['nbEsp']-mins['nbEsp']))**2 + ((nbBases1-nbBases2)/(maxes['nbBases']-mins['nbBases']))**2 + ((diametre1-diametre2)/(maxes['diametre']-mins['diametre']))**2 + {0 si veg1 == veg2, 1 sinon}})
"""


def distance(nbEsp1, nbEsp2, nbBases1, nbBases2, diametre1, diametre2, veg1, veg2):
    v = 0 if veg1 == veg2 else 1
    return math.sqrt(((nbEsp1-nbEsp2)/(maxes['nbEsp']-mins['nbEsp']))**2 + ((nbBases1-nbBases2)/(maxes['nbBases']-mins['nbBases']))**2 + ((diametre1-diametre2)/(maxes['diametre']-mins['diametre']))**2 + v**2)


if __name__ == '__main__':
    print("distance p1 p2 is {}".format(
        distance(11, 5, 1, 2, 120536, 6700, 'oui', 'non')))
    print("distance p1 p3 is {}".format(
        distance(11, 10, 1, 4, 120536, 12756, 'oui', 'oui')))
    print("distance p1 p4 is {}".format(
        distance(11, 7, 1, 2, 120536, 12100, 'oui', 'non')))
    print("distance p1 p5 is {}".format(
        distance(11, 2, 1, 0, 120536, 4880, 'oui', 'non')))
    print("distance p1 p6 is {}".format(
        distance(11, 0, 1, 0, 120536, 2300, 'oui', 'non')))
    print("distance p1 p7 is {}".format(
        distance(11, 8, 1, 2, 120536, 12100, 'oui', 'oui')))

    print("distance p2 p3 is {}".format(
        distance(5, 10, 2, 4, 6700, 12756, 'non', 'oui')))
    print("distance p2 p4 is {}".format(
        distance(5, 7, 2, 2, 6700, 12100, 'non', 'non')))
    print("distance p2 p5 is {}".format(
        distance(5, 2, 2, 0, 6700, 4880, 'non', 'non')))
    print("distance p2 p6 is {}".format(
        distance(5, 0, 2, 0, 6700, 2300, 'non', 'non')))
    print("distance p2 p7 is {}".format(
        distance(5, 8, 2, 2, 6700, 12100, 'non', 'oui')))

    print("distance p3 p4 is {}".format(
        distance(10, 7, 4, 2, 12756, 12100, 'oui', 'non')))
    print("distance p3 p5 is {}".format(
        distance(10, 2, 4, 0, 12756, 4880, 'oui', 'non')))
    print("distance p3 p6 is {}".format(
        distance(10, 0, 4, 0, 12756, 2300, 'oui', 'non')))
    print("distance p3 p7 is {}".format(
        distance(10, 8, 4, 2, 12756, 12100, 'oui', 'oui')))

    print("distance p4 p5 is {}".format(
        distance(7, 2, 2, 0, 12100, 4880, 'non', 'non')))
    print("distance p4 p6 is {}".format(

        distance(7, 0, 2, 0, 12100, 2300, 'non', 'non')))
    print("distance p4 p7 is {}".format(
        distance(7, 8, 2, 2, 12100, 12100, 'non', 'oui')))

    print("distance p5 p6 is {}".format(
        distance(2, 0, 0, 0, 4880, 2300, 'non', 'non')))
    print("distance p5 p7 is {}".format(
        distance(2, 8, 0, 2, 4880, 12100, 'non', 'oui')))

    print("distance p6 p7 is {}".format(
        distance(0, 8, 0, 2, 2300, 12100, 'non', 'oui')))
