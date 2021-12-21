def main():
    n = int(input())
    arr = []
    main_diagonal = 0
    other_diagonal = 0
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # main diagonal elements are always: arr[i][j] where i = j -> arr[i][i]
    for i in range(n):
        main_diagonal += arr[i][i]
    # the other diagonal elements are always: arr[j][n - 1] , arr[j + 1][(n - 1) - 1] --> arr[j][n - 1] and decrement n each iteration.
    for j in range(n):
        other_diagonal += arr[j][n - 1]
        n -= 1
    print(abs(main_diagonal - other_diagonal))


if __name__ == "__main__":
    main()