def main():
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        result = chocolateFeast(n, c, m)
        print(result)


#To be written in hackerrank.
def chocolateFeast(n, c, m):
    # Write your code here
    bars = n // c
    wrappers = bars
    while wrappers >= m:
        wrappers -= m
        bars += 1
        wrappers += 1      
    return bars

if __name__ == '__main__':
    main()