def main():
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for i in range(q):
        queries.append(int(input()))
    for j in range(k):
        last = arr.pop()
        arr.insert(0, last)
    for _ in queries:
        print(arr[_])

if __name__ == '__main__':
    main()