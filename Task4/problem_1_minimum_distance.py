def main():
    numbers = list(map(int, input().split()))
    print(f"first algorithm: {first_approach(numbers)}")
    print(f"second algorithm: {second_approach(numbers)}")


def first_approach(numbers):
    distances = []

    for i in range(0, len(numbers)):
        for j in range(len(numbers) - 1, i, -1):
            if numbers[i] == numbers[j]:
                distances.append(j - i)

    return min(distances)


def second_approach(numbers):
    number_map = dict()
    current = 0
    previous = 0
    min_distance = []
    for i in range(len(numbers)):
        if numbers[i] in number_map:
            current = i
            previous = number_map[numbers[i]]
            min_distance.append(current - previous)
        number_map[numbers[i]] = i
    return min(min_distance)


if __name__ == '__main__':
    main()
