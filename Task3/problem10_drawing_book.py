def main():
    n = int(input().strip())
    p = int(input().strip())
    print(pageCount(n, p))

# because we always turn two pages with one flip
# distance from start is alwasy p // 2
# distance from end is always (n - p) // 2

# To be written in hackerRank.
def pageCount(n, p):
    # Write your code here
    if n != p:
        if n % 2 != 0:
            return min(p // 2, (n - p) // 2)
        elif n % 2 == 0:
            return min(p // 2, (n // 2) - (p // 2))
    else:
        return 0


if __name__ == "__main__":
    main()
