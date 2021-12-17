def main():
    counter = 0
    while True:
        number = int(input())
        if number > 1:
            break
    for i in range (1, number + 1):
        for j in range (1, i + 1):
            if i % j == 0:
                counter += 1
        if counter == 2:
            print(f"{i}", end=" ")
        counter = 0


if __name__ == "__main__":
    main()