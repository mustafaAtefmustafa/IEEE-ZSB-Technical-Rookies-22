import random


def main():
    hit = [0, 0, 0]
    miss = [0, 0, 0]
    n1 = list(str(223))
    print(n1)   # Just for the sake of testing,,, can be removed.
    n2 = list(input("Enter a 3-digit number: "))
    while n2 != n1:
        for i in range(len(n1)):
            if n2[i] == n1[i]:
                hit[i] = 1
            elif n2[i] != n1[i] and n2[i] in  n1:
                miss[i] = 1
        print(f"{sum(hit)} hits {sum(miss)} miss")
        n2 = list(input("Enter a 3-digit number: "))
        hit = [0, 0, 0]
        miss = [0, 0, 0]        

if __name__ == "__main__":
    main()