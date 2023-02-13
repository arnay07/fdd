def get_distance(a, b):
    """
    if a and b are in the distances dict, return the distance
    else if b and a are in the distances dict, return the distance
    """
    if a in distances and b in distances[a]:
        return distances[a][b]
    elif b in distances and a in distances[b]:
        return distances[b][a]
    else:
        raise ValueError('No distance found for %s and %s' % (a, b))


def get_closest(points):
    """
    returns the 2 closest points in a list of points
    """
    closest = (None, None, None)
    for i, a in enumerate(points):
        for b in points[i+1:]:
            distance = get_distance(a, b)
            if closest[2] is None or distance < closest[2]:
                closest = (a, b, distance)
    return closest


if __name__ == '__main__':
    print("this is the single link method")
    points = ['A', 'B', 'C', 'D', 'E']
    distances = {
        'A': {'B': 0.60, 'C': 3.34, 'D': 4.27, 'E': 1.41, 'F': 2.24},
        'B': {'C': 2.78, 'D': 3.66, 'E': 0.84, 'F': 1.74},
        'C': {'D': 1.05, 'E': 1.95, 'F': 1.20},
        'D': {'E': 2.83, 'F': 2.24},
        'E': {'F': 1.00}
    }
    print(get_closest(points))

    points = ['AB', 'C', 'D', 'E', 'F']
    distances = {
        'AB': {'C': 2.78, 'D': 3.66, 'E': 0.84, 'F': 1.74},
        'C': {'D': 1.05, 'E': 1.95, 'F': 1.20},
        'D': {'E': 2.83, 'F': 2.24},
        'E': {'F': 1.00}
    }
    print(get_closest(points))

    points = ['ABE', 'C', 'D', 'F']
    distances = {
        'ABE': {'C': 1.95, 'D': 2.83, 'F': 1.00},
        'C': {'D': 1.05, 'F': 1.20},
        'D': {'F': 2.24}
    }
    print(get_closest(points))

    points = ['ABEF', 'C', 'D']
    distances = {
        'ABEF': {'C': 1.20, 'D': 2.24},
        'C': {'D': 1.05}
    }
    print(get_closest(points))

    points = ['ABEF', 'CD']
    distances = {
        'ABEF': {'CD': 1.20}
    }
    print("----------------------------------")

    print("this is the complete link method")
    points = ['A', 'B', 'C', 'D', 'E', 'F']
    distances = {
        'A': {'B': 0.60, 'C': 3.34, 'D': 4.27, 'E': 1.41, 'F': 2.24},
        'B': {'C': 2.78, 'D': 3.66, 'E': 0.84, 'F': 1.74},
        'C': {'D': 1.05, 'E': 1.95, 'F': 1.20},
        'D': {'E': 2.83, 'F': 2.24},
        'E': {'F': 1.00}
    }
    print(get_closest(points))

    points = ['AB', 'C', 'D', 'E', 'F']
    distances = {
        'AB': {'C': 3.34, 'D': 4.27, 'E': 1.41, 'F': 2.24},
        'C': {'D': 1.05, 'E': 1.95, 'F': 1.20},
        'D': {'E': 2.83, 'F': 2.24},
        'E': {'F': 1.00}
    }
    print(get_closest(points))

    points = ['AB', 'C', 'D', 'EF']
    distances = {
        'AB': {'C': 3.34, 'D': 4.27, 'EF': 2.24},
        'C': {'D': 1.05, 'EF': 1.95},
        'D': {'EF': 2.83}
    }
    print(get_closest(points))

    points = ['AB', 'CD', 'EF']
    distances = {
        'AB': {'CD': 4.27, 'EF': 2.24},
        'CD': {'EF': 2.83}
    }
    print(get_closest(points))

    points = ['ABEF', 'CD']
    distances = {
        'ABEF': {'CD': 4.27}
    }
    print("----------------------------------")

    print("this is the exo 4 of the TD")
    print("single link method")

    points = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
    distances = {
        'P1': {'P2': 0.462, 'P3': 0.666, 'P4': 0.538, 'P5': 0.478, 'P6': 0.334, 'P7': 0.666},
        'P2': {'P3': 0.428, 'P4': 0.466, 'P5': 0.334, 'P6': 0.52, 'P7': 0.786},
        'P3': {'P4': 0.5, 'P5': 0.44, 'P6': 0.652, 'P7': 0.846},
        'P4': {'P5': 0.482, 'P6': 0.52, 'P7': 0.572},
        'P5': {'P6': 0.636, 'P7': 0.76},
        'P6': {'P7': 0.487}
    }

    print(get_closest(points))

    points = ['P1P6', 'P2', 'P3', 'P4', 'P5', 'P7']
    distances = {
        'P1P6': {'P2': 0.462, 'P3': 0.652, 'P4': 0.52, 'P5': 0.478, 'P7': 0.487},
        'P2': {'P3': 0.428, 'P4': 0.466, 'P5': 0.334, 'P7': 0.786},
        'P3': {'P4': 0.5, 'P5': 0.44, 'P7': 0.846},
        'P4': {'P5': 0.482, 'P7': 0.572},
        'P5': {'P7': 0.76}
    }
    print(get_closest(points))

    points = ['P1P6', 'P2P5', 'P3', 'P4', 'P7']
    distances = {
        'P1P6': {'P2P5': 0.462, 'P3': 0.652, 'P4': 0.52, 'P7': 0.487},
        'P2P5': {'P3': 0.428, 'P4': 0.466, 'P7': 0.76},
        'P3': {'P4': 0.5, 'P7': 0.846},
        'P4': {'P7': 0.572}
    }
    print(get_closest(points))

    points = ['P1P6', 'P2P5P3', 'P4', 'P7']
    distances = {
        'P1P6': {'P2P5P3': 0.462, 'P4': 0.52, 'P7': 0.487},
        'P2P5P3': {'P4': 0.466, 'P7': 0.76},
        'P4': {'P7': 0.572}
    }
    print(get_closest(points))

    points = ['P1P6P2P5P3', 'P4', 'P7']
    distances = {
        'P1P6P2P5P3': {'P4': 0.466, 'P7': 0.487},
        'P4': {'P7': 0.572}
    }
    print(get_closest(points))

    points = ['P1P6P2P5P3P4', 'P7']
    distances = {
        'P1P6P2P5P3P4': {'P7': 0.487}
    }
    print(get_closest(points))

    print("----------------------------------")

    print("Complete link method")

    points = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
    distances = {
        'P1': {'P2': 0.462, 'P3': 0.666, 'P4': 0.538, 'P5': 0.478, 'P6': 0.334, 'P7': 0.666},
        'P2': {'P3': 0.428, 'P4': 0.466, 'P5': 0.334, 'P6': 0.52, 'P7': 0.786},
        'P3': {'P4': 0.5, 'P5': 0.44, 'P6': 0.652, 'P7': 0.846},
        'P4': {'P5': 0.482, 'P6': 0.52, 'P7': 0.572},
        'P5': {'P6': 0.636, 'P7': 0.76},
        'P6': {'P7': 0.487}
    }
    print(get_closest(points))

    points = ['P1P6', 'P2', 'P3', 'P4', 'P5', 'P7']
    distances = {
        'P1P6': {'P2': 0.52, 'P3': 0.666, 'P4': 0.538, 'P5': 0.636, 'P7': 0.666},
        'P2': {'P3': 0.428, 'P4': 0.466, 'P5': 0.334, 'P7': 0.786},
        'P3': {'P4': 0.5, 'P5': 0.44, 'P7': 0.846},
        'P4': {'P5': 0.482, 'P7': 0.572},
        'P5': {'P7': 0.76}
    }
    print(get_closest(points))

    points = ['P1P6', 'P2P5', 'P3', 'P4', 'P7']
    distances = {
        'P1P6': {'P2P5': 0.636, 'P3': 0.666, 'P4': 0.538, 'P7': 0.666},
        'P2P5': {'P3': 0.44, 'P4': 0.482, 'P7': 0.786},
        'P3': {'P4': 0.5, 'P7': 0.846},
        'P4': {'P7': 0.572}
    }
    print(get_closest(points))

    points = ['P1P6', 'P2P5P3', 'P4', 'P7']
    distances = {
        'P1P6': {'P2P5P3': 0.666, 'P4': 0.538, 'P7': 0.666},
        'P2P5P3': {'P4': 0.5, 'P7': 0.846},
        'P4': {'P7': 0.572}
    }
    print(get_closest(points))

    points = ['P1P6', 'P2P5P3P4', 'P7']
    distances = {
        'P1P6': {'P2P5P3P4': 0.666, 'P7': 0.666},
        'P2P5P3P4': {'P7': 0.846}
    }
    print(get_closest(points))

    points = ['P1P6P2P5P3P4', 'P7']
    distances = {
        'P1P6P2P5P3P4': {'P7': 0.846}
    }
    print(get_closest(points))
