def main():
    length = int(input())
    width = int(input())
    print(area(length, width))
    print(perimeter(length, width))


def area(length, width):
    area = length * width
    return area


def perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter


if __name__ == "__main__":
    main()