def main():
    q = int(input())
    for i in range(q):
        s = input()
        result = hacker_rank_in_string(s)
        print(result)

# To be written in hackerRank
def hacker_rank_in_string(s):
    string = "hackerrank"
    j = 0
    if len(s) < len(string):
        return "NO"
    else:
        for i in range(len(s)):
            if j < len(string) and s[i] == string[j]:
                j += 1
        
    if j == len(string):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    main()