def main():
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    for _ in arr:
        _ += d
        if _ in arr:
            _ += d
            if _ in arr:
                count += 1
    print(count)


if __name__ == '__main__':
    main()