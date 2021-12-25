def main():
    x1, v1, x2, v2 = map(int, input().strip().split())

    result = kangaroo(x1, v1, x2, v2)
    
    print(result)

#  To be written in hackerRank
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    while True:
        if v2 > v1 or v2 == v1:
            return "NO"
        
        else:
            x1 += v1 
            x2 += v2
            if x1 == x2:
                return "YES"
            elif x1 > x2:
                return "NO"
            else:
                continue

if __name__ == "__main__":
    main()