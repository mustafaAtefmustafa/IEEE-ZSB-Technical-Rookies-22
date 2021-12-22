def main():
    l = [5, 9, 5, 3, 10, 100, 150, 90, 50]
    print(insertionsort(l))


def insertionsort(l):
    for j in range(1, len(l)):
        key = l[j]
        i = j - 1
        while (i >= 0) and (l[i] > key):
            l[i + 1] = l[i]
            i -= 1
        l[i + 1] = key
    return l


if __name__ == "__main__":
    main()
