def main():
    string = input()
    sub_string = input()
    n = count_sub_string(string, sub_string)
    print(n)


def count_sub_string(string, sub_string):
    start = 0
    counter = 0
    i = 0
    while i < len(string):
        if string[i] == sub_string[start]:
            start += 1
        if start == len(sub_string):
            start = 0
            counter += 1
            i -= 1
        i += 1
    return counter


if __name__ == "__main__":
    main()