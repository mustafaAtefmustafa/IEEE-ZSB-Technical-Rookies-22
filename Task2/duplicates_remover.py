def main():
    numbers = list(map(int, input().split()))
    for i in range(len(numbers) - 1, -1, -1):   # reading the list from the end so we abvoid any index issues.
        if numbers[i] == numbers[i - 1]:
            numbers.remove(numbers[i - 1])
    print(numbers)

if __name__ == "__main__":
    main()
