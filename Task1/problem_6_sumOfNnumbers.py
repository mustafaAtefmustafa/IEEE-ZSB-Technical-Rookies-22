def main():
    while True:
        n = int(input())
        if n > 1:
            break
    sum = 0
    for i in range(0, n + 1):
        sum += i
    print(sum)


if __name__ == "__main__":
    main()
