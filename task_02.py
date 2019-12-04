def get_input():
    with open("input/input_02.txt") as fin:
        array = [int(element.strip()) for element in fin.read().split(",")]
        array[1] = 12
        array[2] = 2
        return array


def get_result(initial):
    array = initial[:]
    index = 0
    while True:
        opcode = array[index]
        if opcode == 99:
            break
        first = array[array[index+1]]
        second = array[array[index+2]]
        if opcode == 1:
            array[array[index+3]] = first + second
        if opcode == 2:
            array[array[index+3]] = first * second
        index += 4
    return array[0]


def main():
    array = get_input()
    result = get_result(array)
    print(result)
    for first in range(100):
        for second in range(100):
            array[1] = first
            array[2] = second
            result = get_result(array)
            if result == 19690720:
                answer = 100 * first + second
                print(answer)
                return


if __name__ == "__main__":
    main()
