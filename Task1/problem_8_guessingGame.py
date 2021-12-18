import random


def main():
    counter = 1
    n = random.randint(1, 10)
    print("Guess the number")

    while True:
        x = int(input())
        if x == n:
            break
        else:
            counter += 1
            print("Try again!")

    print(f"U'RE GODDAMN RIGHT! After {counter} tries!")


if __name__ == "__main__":
    main()
