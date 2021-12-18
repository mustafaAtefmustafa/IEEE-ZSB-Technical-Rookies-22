def main():
    n = int(input())
    for i in range(0, n):
        print(f"{get_fib(i)}", end=" ")


def get_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fib(n - 1) + get_fib(n - 2)


if __name__ == "__main__":
    main()
