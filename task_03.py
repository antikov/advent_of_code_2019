from math import inf

mapping = {
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0)
}


def preprocess_paths(path):
    return [(way.strip()[0], int(way.strip()[1:])) for way in path.split(",")]


def generate_wire(path):
    x, y = 0, 0
    wire = set()
    for direction, distance in path:
        dx, dy = mapping[direction]
        for _ in range(distance):
            x += dx
            y += dy
            wire.add((x, y))
    return wire

def get_input():
    with open("input/input_03.txt") as fin:
        path1, path2 = fin.read().strip().split("\n")
        return preprocess_paths(path1), preprocess_paths(path2)


def get_min_distance(wire1, wire2):
    _min = inf
    for el in wire1:
        if el in wire2:
            _sum = abs(el[0]) + abs(el[1])
            _min = _sum if _min > _sum else _min
    return _min


def combined_steps(path, wire):
    x, y = 0, 0
    total = 0
    mm = {}
    for direction, distance in path:
        dx, dy = mapping[direction]
        for _ in range(distance):
            total += 1
            x += dx
            y += dy
            if (x, y) in wire and (x, y) not in mm:
                mm[(x, y)] = total
    return mm


def get_fewest_steps(path1, path2, wire1, wire2):
    mm1 = combined_steps(path1, wire2)
    mm2 = combined_steps(path2, wire1)
    mm = {key:mm1[key] + mm2[key] for key in mm1.keys()}
    return min(mm.values())


def main():
    path1, path2 = get_input()
    wire1, wire2 = generate_wire(path1), generate_wire(path2)
    result1 = get_min_distance(wire1, wire2)
    result2 = get_fewest_steps(path1, path2, wire1, wire2)
    print(result1, result2)
    return


if __name__ == "__main__":
    main()
