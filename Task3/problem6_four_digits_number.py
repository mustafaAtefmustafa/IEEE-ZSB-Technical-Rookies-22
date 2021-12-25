def main():
    c = 0
    while True:
        number = int(input())
        if len(str(number)) == 4:  # Making sure it's a 4 digit number.
            # Making sure it has a distinct digit.
            for i in range(1, len(str(number))):
                if str(number)[0] != str(number)[i]:
                    break
                else:
                    c += 1
            if c == 3:
                print("please enter a valid number!")
                c = 0
                continue
            else:
                break
        print("please enter a valid number!")
    counter = 1
    while True:
        n1 = int("".join(sorted([i for i in str(number)], reverse=True)))
        n2 = int("".join(sorted([i for i in str(number)])))
        number = n1 - n2
        if len(str(number)) == 3:
            number = int(str(number) + "0")
        if number == 6174:
            break
        else:
            counter += 1
            continue
    print(counter)


if __name__ == "__main__":
    main()
