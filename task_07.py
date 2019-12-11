from itertools import permutations
from math import inf


def get_input():
    with open("input/input_07.txt") as fin:
        array = [int(element.strip()) for element in fin.read().split(",")]
        return array


def get_result(initial, inp):
    array = initial[:]
    index = 0
    output = []
    input_index = 0
    while True:
        temp = array[index]
        opcode = temp % 100
        flag_1 = temp % 1000 // 100
        flag_2 = temp % 10000 // 1000
        if opcode == 99:
            break
        if opcode in [1, 2]:
            first = array[index+1] if flag_1 else array[array[index+1]]
            second = array[index+2] if flag_2 else array[array[index+2]]
            if opcode == 1:
                array[array[index+3]] = first + second
            else:
                array[array[index+3]] = first * second
            index += 4
        elif opcode == 3:
            array[array[index+1]] = inp[input_index]
            input_index += 1
            index += 2
        elif opcode == 4:
            first = array[index+1] if flag_1 else array[array[index+1]]
            output.append(first)
            index += 2
        elif opcode in [5, 6]:
            first = array[index+1] if flag_1 else array[array[index+1]]
            second = array[index+2] if flag_2 else array[array[index+2]]
            if (opcode == 5 and first) or (opcode == 6 and not first):
                index = second
            else:
                index += 3
        elif opcode in [7, 8]:
            first = array[index+1] if flag_1 else array[array[index+1]]
            second = array[index+2] if flag_2 else array[array[index+2]]
            if opcode == 7:
                array[array[index+3]] = 1 if first < second else 0
            if opcode == 8:
                array[array[index+3]] = 1 if first == second else 0
            index += 4

    return output[0]


def main():
    initial_array = get_input()
    max_result = -inf
    for signal in permutations(range(5)):
        result = 0
        for index in range(5):
            result = get_result(initial_array, [signal[index], result])
        if result > max_result:
            max_result = result
    print(max_result)


if __name__ == "__main__":
    main()
