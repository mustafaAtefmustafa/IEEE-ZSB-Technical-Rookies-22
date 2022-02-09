def main():
    letters = input()
    n = int(input())
    print(f"First method: {first_approach(letters, n)}")
    print(f"Second method: {second_approach(letters, n)}")


def first_approach(letters, n):
    seq = ''
    count = 0
    while len(seq) < n:
        for i in range(len(letters)):
            seq += letters[i]
            if(len(seq) == n):
                break
    for j in seq:
        if j == 'r':
            count += 1
    return count


def second_approach(letters, n):
    count = 0
    if n % len(letters) == 0:
        for i in letters:
            if i == 'r':
                count += 1
        return (n / len(letters)) * count
    else:
        count2 = 0
        for i in letters:
            if i == 'r':
                count += 1
        for j in range(n % len(letters)):
            if letters[j] == 'r':
                count2 += 1
        return ((n // len(letters)) * count) + count2


if __name__ == '__main__':
    main()
