def main():
    steps = int(input().strip())

    while True:
        path = input()
        if len(path) == steps:
            break
        print("please enter the right path!")

    result = countingValleys(steps, path)
    print(result)


def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    counter = 0
    for i in path:
        if i == "U":
            sea_level += 1
        elif i == "D":
            sea_level -= 1
        if sea_level == 0 and i == "U":
            counter += 1
    return counter


if __name__ == "__main__":
    main()
