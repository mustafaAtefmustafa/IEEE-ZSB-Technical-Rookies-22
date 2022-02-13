def main():
    n1 = list(map(int, input().split()))
    days = n1[0]
    reading_time = n1[1]
    number_of_seconds_left = 86400
    count = 1
    n2 = list(map(int, input().split()))
    if len(n2) != days:
        print("Invalid")
        return
    for i in range(days):
        number_of_seconds_left -= n2[i]
        if number_of_seconds_left == 0:
            count += 1
            number_of_seconds_left = 86400
            continue
        else:
            if number_of_seconds_left >= reading_time:
                print(count)
                break
            else:
                reading_time -= number_of_seconds_left
                count += 1
                number_of_seconds_left = 86400
                continue


if __name__ == '__main__':
    main()
