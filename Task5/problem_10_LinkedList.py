def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        popularity = list(map(int, input().split()))
        result = delete(n, popularity, k)
        print(*result)

def delete(n, popularity, k):
    arr = []
    for i in popularity:
        while len(arr) > 0 and i > arr[-1] and k > 0:
            arr.pop()
            k -= 1
        arr.append(i)
    return arr
if __name__ == '__main__':
    main()
