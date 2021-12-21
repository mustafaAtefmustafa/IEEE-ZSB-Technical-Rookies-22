import random


def main():
    hit_counter = 0
    miss_counter = 0
    n1 = list(str(random.randint(100, 999)))
    print(n1)   # Just for the sake of testing,,, can be removed.
    n2 = list(input("Enter a 3-digit number: "))
    while n2 != n1:
        for i in range(0, len(n2)):
            for j in range(0, len(n1)):
                if n2[i] == n1[j] and i == j:
                    hit_counter += 1
                    break
                elif n2[i] == n1[j] and i != j:
                    miss_counter += 1
                    break
                else:
                    continue
        print(f"{hit_counter} hit  {miss_counter} miss")
        n2 = list(input("Enter a 3-digit number: "))
        hit_counter = 0
        miss_counter = 0


if __name__ == "__main__":
    main()