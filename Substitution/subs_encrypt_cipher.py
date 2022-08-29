def encrypt_substitution_cipher(plain_text, key):
    result = ""
    for char in plain_text:
        if char in key:
            result += key[char]
        else:
            result += char
    return result


def main():
    plain_text = input("Enter the plain text:- ")
    alphabets = {}
    for i in range(65, 91):
        char = input("Enter the character for " + chr(i) + ":- ")
        alphabets[chr(i)] = char
        alphabets[chr(i+32)] = chr(ord(char)+32)
    encrypted_text = encrypt_substitution_cipher(plain_text, alphabets)
    print(alphabets)
    print("Encrypted text:- " + encrypted_text)


if __name__ == "__main__":
    main()
