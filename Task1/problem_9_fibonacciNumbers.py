def main():
    n = int(input())

    # Bad algorithm.
    """for i in range(0, n):
        print(f"{get_fib(i)}", end=" ")"""

    # Better algorithm.
    l = [0, 1]
    for i in range(0, n - 2):
        l.append(l[-1] + l[-2])
    print(l)


"""def get_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fib(n - 1) + get_fib(n - 2)"""


if __name__ == "__main__":
    main()
