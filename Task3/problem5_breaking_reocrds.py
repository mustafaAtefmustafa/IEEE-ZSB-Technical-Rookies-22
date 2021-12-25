def main():
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)


# To be written in hackerRank.
def breakingRecords(scores):
    # Write your code here
    highest_score = lowest_score = scores[0]
    result = [0, 0]
    for i in range(1, len(scores)):
        if scores[i] > highest_score:
            highest_score = scores[i]
            result[0] += 1
        elif scores[i] < lowest_score:
            lowest_score = scores[i]
            result[1] += 1
        else:
            continue
    return result


if __name__ == "__main__":
    main()
