def main():
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

# To be written in hackerRank.
def getTotalX(a, b):
    # Write your code here
    total = 0
    a = sorted(a)
    b = sorted(b)
    candidates = []
    # Get all candidates between the two lists.
    for i in b:
        for j in range(a[-1], b[0] + 1):
            if (i % j) == 0 and j >= a[-1] and j <= b[0]:
                candidates.append(j)

    candidates = list(set(candidates))   # Remove duplicates.
    # Remove candidates that has no factors in first list
    for o in range(len(candidates) - 1, -1, -1):
        for u in a:
            if candidates[o] % u != 0:
                candidates.remove(candidates[o])
                break
            else:
                continue
    # get the total numbers satisfy the conditions.
    for k in candidates:
        for s in b:
            if s % k != 0:
                break
        else:
            total += 1

    return total


if __name__ == "__main__":
    main()
