def main():
    arr_count = int(input().strip())
    while True:
        arr = list(map(int, input().rstrip().split()))
        if len(arr) == arr_count:
            break
        else:
            print("please enter a valid array!")
    result = migratoryBirds(arr)
    print(result)


# To be written in hackerRank.
def migratoryBirds(arr):
    # Write your code here
    bird_types = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]

    for i in arr:
        if i == 1:
            bird_types[0][0] += 1
        elif i == 2:
            bird_types[1][0] += 1
        elif i == 3:
            bird_types[2][0] += 1
        elif i == 4:
            bird_types[3][0] += 1
        else:
            bird_types[4][0] += 1

    max_frequency = sorted(bird_types)[-1][0]
    l = []

    for j in sorted(bird_types):
        if j[0] == max_frequency:
            l.append(j)
    return l[0][1]


if __name__ == "__main__":
    main()
