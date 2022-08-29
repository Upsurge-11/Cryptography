def decrypt_substitution(text, key):
    result = ""
    alphabet_mapping = {}
    translation = {}
    for c in text:
        char = c.upper()
        if char in alphabet_mapping:
            alphabet_mapping[char] += 1
        else:
            alphabet_mapping[char] = 0
    alphabet_mapping = {key: val for key, val in sorted(
        alphabet_mapping.items(), key=lambda ele: ele[1], reverse=True)}
    key_list = list(alphabet_mapping.keys())
    j = 1
    for i in range(len(key_list)):
        translation[key_list[i]] = key[j]
        j += 1
    for char in text:
        if char in translation:
            result += translation[char]
        else:
            result += char

    return result


def remove_spaces(s):
    return s.replace(" ", "")


def main():
    encrypted_text = input("Enter the encrypted text:- ")
    encrypted_text = encrypted_text.upper()
    encrypted_text = remove_spaces(encrypted_text)
    alphabets = {
        1: 'E', 2: 'T', 3: 'A', 4: 'O', 5: 'I', 6: 'N', 7: 'S', 8: 'H', 9: 'R', 10: 'D', 11: 'L', 12: 'C', 13: 'U', 14: 'M', 15: 'W', 16: 'F', 17: 'G', 18: 'Y', 19: 'P', 20: 'B', 21: 'V', 22: 'K', 23: 'J', 24: 'Q', 25: 'X', 26: 'Z'
    }
    decrypted_text = decrypt_substitution(encrypted_text, alphabets)
    print("Decrypted text:- " + decrypted_text)


if __name__ == "__main__":
    main()
