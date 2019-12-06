from collections import deque, defaultdict


def get_input():
    mapping = {}
    reverse = defaultdict(list)
    with open("input/input_06.txt") as fin:
        for element in fin.readlines():
            left, right = element.strip().split(")")
            mapping[right] = left
            reverse[left].append(right)
        return mapping, reverse


def main():
    mapping, reverse = get_input()
    total = 0
    for key in mapping.keys():
        current_key = key
        while mapping.get(current_key, None) is not None:
            total += 1
            current_key = mapping[current_key]
    print(total)

    stack = deque([("YOU", 0)])
    visited = set()
    while stack:
        key, value = stack.popleft()
        visited.add(key)
        if key == "SAN":
            print(value - 2)
            break
        if mapping.get(key, None) not in visited:
            stack.append((mapping.get(key, None), value + 1))
        for el in reverse.get(key, []):
            if el not in visited:
                stack.append((el, value + 1))


if __name__ == "__main__":
    main()
