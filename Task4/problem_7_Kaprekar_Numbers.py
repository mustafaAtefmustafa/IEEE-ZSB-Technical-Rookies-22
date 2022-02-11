def kaprekarNumbers(p, q):
    # Write your code here
    count = 0
    for i in range(p, q + 1):
        d1 = len(str(i))
        beta = pow(i, 2) % pow(10, d1)
        alpha = (pow(i, 2) - beta) // pow(10, d1)
        if (alpha + beta) == i:
            print(i, end=" ")
            count += 1
        else:
            continue
    if count == 0:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
