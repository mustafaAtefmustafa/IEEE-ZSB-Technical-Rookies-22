import string
import secrets


def main():
    special_characters = ["@", "#", "$", "%", "&"]
    alphabet = string.ascii_letters + string.digits + secrets.choice(special_characters)
    while True:
        password = "".join(secrets.choice(alphabet) for i in range(10))
        if sum(element.isdigit() for element in password) >= 1 and sum(e in special_characters for e in password) >= 1:
            break

    print(password)


if __name__ == "__main__":
    main()
