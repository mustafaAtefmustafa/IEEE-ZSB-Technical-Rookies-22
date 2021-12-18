def main():
    words = input().split()
    longest_word = 0
    for word in words:
        if len(word) > longest_word:
            longest_word = len(word)
    print('*' * longest_word + '****')

    for word in words:
        print('* ' + word.ljust(longest_word + 1) + '*')

    print('*' * longest_word + '****')


if __name__ == "__main__":
    main()