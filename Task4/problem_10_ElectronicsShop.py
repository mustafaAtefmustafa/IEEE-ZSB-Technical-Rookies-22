# The function to be written in hackerRank.
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    final_cost = []
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                final_cost.append(i + j)
    if len(final_cost) == 0:
        return -1
    else:
        return max(final_cost)


if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)