# The function to be written in hackerRank
def stones(n, a, b):
    minimum = min(a, b) * (n-1)
    maximum = max(a, b) * (n-1)
    difference = abs(b - a)
    arr = []
    if a == b:
        arr.append(minimum)
    else:
        while minimum <= maximum:
            arr.append(minimum)
            minimum += difference
    return arr


if __name__ == '__main__':

    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    result = stones(n, a, b)
    print(result)
