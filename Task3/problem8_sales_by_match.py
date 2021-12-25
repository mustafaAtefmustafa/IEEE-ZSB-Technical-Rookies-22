def main():
    n = int(input().strip())
    while True:
        ar = list(map(int, input().rstrip().split()))
        if len(ar) == n:
            break
        else:
            print("please enter a valid array!")
    result = sockMerchant(n, ar)
    print(result)


# To be written in hackerRank
def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    counter = 0
    arr = list(set(ar))  # remove duplicates
    for i in arr:
        for j in ar:
            if i == j:
                counter += 1
        pairs += counter // 2
        counter = 0
    return pairs


if __name__ == "__main__":
    main()
