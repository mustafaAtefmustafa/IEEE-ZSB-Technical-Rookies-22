def main():
    string = input()
    sub_string = input()
    n = count_sub_string(string, sub_string)
    print(n)


def count_sub_string(string, sub_string):
    counter = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
            
    return counter


if __name__ == "__main__":
    main()