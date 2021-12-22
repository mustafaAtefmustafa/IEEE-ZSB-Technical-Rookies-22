def main():
    n = int(input())
    arr = map(int, input().split())
    arr2 = sorted(arr)
    arr3 = []  # just so we don't remove scores from our original list.
    for i in arr2:
        if i in arr3:
            continue
        arr3.append(i)
    print(arr3[-2])


if __name__ == "__main__":
    main()
