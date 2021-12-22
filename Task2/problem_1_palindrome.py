def main():
    word = input()
    word = list(word)
    word_reverted = word[::-1]
    if word == word_reverted:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
