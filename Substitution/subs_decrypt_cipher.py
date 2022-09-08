def decrypt_substitution_cipher(text, size):
    plaintext = [None] * 26
    key = "ETAOINSHRDLCUMWFGYPBVKJQXZ"
    freq = [0] * 26
    freqSorted = [None] * 26
    used = [0] * 26

    for i in range(size):
        if text[i] != ' ':
            freq[ord(text[i]) - 65] += 1

    for i in range(26):
        freqSorted[i] = freq[i]

    freqSorted.sort(reverse=True)

    for i in range(26):
        ch = -1
        for j in range(26):
            if freqSorted[i] == freq[j] and used[j] == 0:
                used[j] = 1
                ch = j
                break
        if ch == -1:
            break
        x = ord(key[i]) - 65
        x = x - ch
        curr = ""
        for k in range(size):
            if text[k] == ' ':
                curr += " "
                continue
            y = ord(text[k]) - 65
            y += x
            if y < 0:
                y += 26
            if y > 25:
                y -= 26
            curr += chr(y + 65)
        plaintext[i] = curr

    for i in range(26):
        print(str(i+1) + ") " + plaintext[i])


def main():
    encrypted_text = input("Enter the string :- ")
    decrypt_substitution_cipher(encrypted_text.upper(), len(encrypted_text))


if __name__ == "__main__":
    main()
