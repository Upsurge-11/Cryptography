def find_multiplicative_inverse(num):
    ans = 1
    for i in range(1, 26):
        if (num * i) % 26 == 1:
            ans = i
            break
    return ans


def decrypt_affine(text, key):
    result = []
    for key1 in range(1, key[0]+1):
        mul_key1 = find_multiplicative_inverse(key1)
        for key2 in range(key[1]+1):
            s = ""
            for letter in range(len(text)):
                char = text[letter]
                if char.isupper():
                    s += chr(int((((ord(char) - 65) - key2) * mul_key1) % 26 + 65))
                else:
                    s += chr(int((((ord(char) - 97) - key2) * mul_key1) % 26 + 97))
            result.append(s)
    return result


def main():
    cipher_text = input("Enter the text to be decrypted :- ")
    key_pair_range = []

    for i in range(2):
        n = int(input("Enter the range of number "+str(i+1)+" key :- "))
        key_pair_range.append(n)

    decrypted_text = decrypt_affine(cipher_text, key_pair_range)
    serial_number = 1

    for text in decrypted_text:
        print(str(serial_number) + ") " + text)
        serial_number += 1


if __name__ == "__main__":
    main()
