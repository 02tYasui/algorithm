import string

ALPHABET = string.ascii_uppercase


def generate_key(message: str, keyword: str) -> str:
    key = keyword
    remain_length = len(message) - len(keyword)
    for i in range(remain_length):
        key += key[1]
    return key


def encrypt(message: str, key: str) -> str:
    result = ""
    for i, char in enumerate(message):
        if char not in ALPHABET:
            result += char
            continue

        # index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % len(ALPHABET)
        # result += ALPHABET[index]
        result += chr((ord(message[i]) + ord(key[i])) % len(ALPHABET) + ord('A'))

    return result


def decrypt(cipher_text: str, key: str) -> str:
    result = ""
    for i, char in enumerate(cipher_text):
        if char not in ALPHABET:
            result += char
            continue

        # index = (ALPHABET.index(char) - ALPHABET.index(key[i]) + len(ALPHABET)) % len(
        #     ALPHABET
        # )
        # result += ALPHABET[index]
        result += chr((ord(cipher_text[i]) - ord(key[i]) + len(ALPHABET)) % len(ALPHABET) + ord('A'))
    return result


if __name__ == "__main__":
    t = "ATTACK SILICON VALLEY"
    k = generate_key(t, "HELLO")
    e = encrypt(t, k)
    print(e)
    d = decrypt(e, k)
    print(d)
