def main():
    max_volume = 0
    max_capacity = []
    cap = []

    while True:
        bottles = int(input())
        if bottles > 1:
            break

    for i in range(bottles):
        volume , capacity = map(int,input().strip().split())
        max_volume += volume
        cap.append(capacity)

    for j in range(len(cap)):
        for k in cap[j + 1:]:
            max_capacity.append(cap[j] + k)

    max_capacity = sorted(max_capacity)
    if max_volume <= max_capacity[0]:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()