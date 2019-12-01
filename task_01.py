from math import floor


def get_input():
    with open("input/input_01.txt") as fin:
        return [int(element) for element in fin.readlines()]


def get_fuel(initial):
    return floor(initial / 3 - 2)


def main():
    masses = get_input()
    result1, result2 = 0, 0
    for mass in masses:
        current = get_fuel(mass)
        result1 += current

        while current > 0:
            result2 += current
            current = get_fuel(current)

    print(result1, result2)


if __name__ == "__main__":
    main()
