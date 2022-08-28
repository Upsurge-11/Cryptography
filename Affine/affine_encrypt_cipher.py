def affine_encrypt(text, key):
    result = ""
    for letter in range(len(text)):
        char = text[letter]
        if char.isupper():
            result += chr(((ord(char) - 65) * key[0] + key[1]) % 26 + 65)
        else:
            result += chr(((ord(char) - 97) * key[0] + key[1]) % 26 + 97)
    return result


def main():
    plain_text = input("Enter the plain text in here :- ")
    key_pairs = []

    for i in range(2):
        n = int(input("Enter the key " + str(i) + " :- "))
        key_pairs.append(n)

    encrypted_text = affine_encrypt(plain_text, key_pairs)
    print(encrypted_text)


if __name__ == "__main__":
    main()
