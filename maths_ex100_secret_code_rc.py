'''
Name: Raul Costa
Date: 29/04/2022

EC148003 Software Development with Applied Mathematics with Python

Problem: decipher the SECRET_CODE and then find and identify the creature.

From the cyphertext take each number mod 42 it and then map it to the following:
    0-25    -   lowercase alphabet (az)
    26      -   fullstop (.)


Using https://what3words.com  and remaining in the UK, what type of creature can see?

'''
from string import ascii_lowercase

def decrypt(cyphertext):

    plaintext = ''
    codelist = []
    ascii = list(ascii_lowercase)
    ascii.append(' ')
    for i in range(len(cyphertext)):
        code = cyphertext[i] % 42
        letter = ascii[code]
        plaintext += letter

    return plaintext


def main():
    secret_code = [313, 126, 309, 298, 312, 194, 312,
                   168, 215, 130, 271, 318, 152, 145, 217, 302, 139]

    plaintext = decrypt(secret_code)
    print(plaintext)


if __name__ == "__main__":
    main()
