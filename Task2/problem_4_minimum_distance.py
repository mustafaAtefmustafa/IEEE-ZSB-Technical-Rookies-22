def main():
    numbers = list(map(int, input().split()))
    distances = []  # A list to store the distance of any matched element.
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                distances.append(j - i)
    distances = sorted(distances)
    print(distances[0])


if __name__ == "__main__":
    main()
