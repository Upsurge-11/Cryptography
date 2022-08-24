def caesar_decrypt(text, brute_force_num):
    result = []
    for key in range(1, brute_force_num + 1):
        s = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                s += chr((ord(char) - key - 65) % 26 + 65)
            else:
                s += chr((ord(char) - key - 97) % 26 + 97)
        result.append(s)
    return result


cipher_text = input("Enter the text :- ")
n = int(input("Enter the range of key to use for brute force :- "))

decrypted_text = caesar_decrypt(cipher_text, n)

shift_key_number = 1

for ans in decrypted_text:
    print(str(shift_key_number) + ') ', ans)
    shift_key_number += 1
