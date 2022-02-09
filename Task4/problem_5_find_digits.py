def main():
    num = int(input())
    for i in range(num):
        n = int(input())
        result = findDigits(n)
        print(result)


#To be written in hackerrank.        
def findDigits(n):
    # Write your code here
    count = 0
    number = str(n)
    for i in range(len(number)):
        if int(number[i]) != 0 and n % int(number[i]) == 0:
            count += 1
    return count


if __name__ == '__main__':
    main()
