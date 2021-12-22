import random


def main():
    hit = [0, 0, 0]
    miss = [0, 0, 0]
    n1 = list(str(random.randint(100, 999)))
    print(n1)   # Just for the sake of testing,,, can be removed.
    n2 = list(input("Enter a 3-digit number: "))
    while n2 != n1:
        for i in range(0, len(n2)):
            for j in range(0, len(n1)):
                if n2[i] == n1[j] and i == j:
                    hit[i] = 1
                    miss[i] = 0
                    break
                elif n2[i] == n1[j] and i != j:
                    
                    if hit[j] == 1:
                        #miss[i] = 1
                        continue
                    else:
                        miss[j] = 1
                        continue
                else:
                    continue
        hits = sum(hit)
        misses = sum(miss)
        print(f"{hits} hit  {misses} miss")
        n2 = list(input("Enter a 3-digit number: "))
        hit = [0, 0, 0]
        miss = [0, 0, 0]
    


if __name__ == "__main__":
    main()