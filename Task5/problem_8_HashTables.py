def delete_friends(friends, k):
    arr = []
    for i in friends:
        while len(arr) > 0 and arr[-1] < i and k > 0:
            arr.pop()
            k -= 1
        arr.append(i)
    return arr


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        friends = list(map(int, input().split()))
        result = delete_friends(friends, k)
        print(*result)