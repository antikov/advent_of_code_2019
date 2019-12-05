def get_input():
    return 256310, 732736


def is_satisfied_condition(number):
    number = list(number)
    first = number[0]
    double_flag = False
    for second in number[1:]:
        if first > second:
            return False
        if first == second:
            double_flag = True
        first = second
    return double_flag


def is_satisfied_second_condition(number):
    number = list(number)
    first = number[0]
    for second in number[1:]:
        if first > second:
            return False
        first = second

    first = number[0]
    _count = 1
    for second in number[1:]+['!']:
        if second == first:
            _count += 1
        else:
            if _count == 2:
                return True
            _count = 1
            first = second
    return False


def main():
    min_range, max_range = get_input()
    result1 = 0
    result2 = 0
    for number in range(min_range, max_range):
        result1 += 1 if is_satisfied_condition(str(number)) else 0
        result2 += 1 if is_satisfied_second_condition(str(number)) else 0
    print(result1, result2)


if __name__ == "__main__":
    main()
