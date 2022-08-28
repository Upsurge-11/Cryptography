def caesar_encrypt(message, key):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result


def main():
    text = input("Enter the string :- ")
    s = int(input("Enter the key :- "))

    encrypted_message = caesar_encrypt(text, s)
    print(encrypted_message)


if __name__ == "__main__":
    main()
