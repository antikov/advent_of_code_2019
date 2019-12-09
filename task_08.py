from collections import Counter
from math import inf


W = 25
T = 6


def get_input():
    with open("input/input_08.txt") as fin:
        result = []
        colors = fin.read().strip()
        for layer_index in range(len(colors)//(W*T)):
            result.append(colors[layer_index*W*T:(layer_index+1)*W*T])
        return result


def get_count(layer, digit):
    return Counter(layer)[str(digit)]


def main():
    layers = get_input()
    fewest_layer = 0
    fewest_zeros = inf
    for index, layer in enumerate(layers):
        current_zeros = get_count(layer, 0)
        if current_zeros < fewest_zeros:
            fewest_zeros = current_zeros
            fewest_layer = index
    layer = layers[fewest_layer]
    result = get_count(layer, 1) * get_count(layer, 2)
    print(result)

    render = [None] * (W * T)
    
    for index in range(len(render)):
        for layer in layers:
            if layer[index] != "2":
                render[index] = " " if layer[index] == "0" else "X"
                break

    for t in range(T):
        for w in range(W):
            print(render[t*W+w],end="")
        print()


if __name__ == "__main__":
    main()
