def main():
    n = int(input())
    l = list(map(int, input().split()))
    print(sum_with_for(n, l))
    print(sum_with_while(n, l))
    print(sum_with_recursion(l))

def sum_with_for(n, l):
    sum = 0
    for i in l:
        sum += i
    return sum

def sum_with_while(n, l):
    sum = 0
    j = 0
    while j <= (n - 1):
        sum += l[j]
        j += 1
    return sum

def sum_with_recursion(l):
    if len(l) == 0:
        return 0
    else:
         return l[0] + sum_with_recursion(l[1:])

if __name__ == "__main__":
    main()