def main():
    n, m = map(int,input().split())
    attendee = []
    l= []
    for i in range(n):
        x = input()
        attendee.append(x)
    for j in range(n):
        for k in range(j + 1, n):
            l.append(bin((int(attendee[j],2)) | (int(attendee[k],2))).count('1'))
    max_score = max(l)
    print(max_score)
    print(l.count(max_score))

if __name__ == '__main__':
    main()