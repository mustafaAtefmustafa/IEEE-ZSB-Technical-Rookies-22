def main():
    l = [1, 2, 5, 9]
    x = int(input())
    res = binary_search(l, x)
    if res != -1:
        print("found!")
    else:
        print("not found!")


def binary_search(l, x):
    if len(l) > 0:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid + 1:]
        if x == l[mid]:
            return mid
        elif x < l[mid]:
            return binary_search(left, x)
        else:
            return binary_search(right, x)
    else:
        return -1

if __name__ == "__main__":
    main()
