import sys
import math

# Fonctions
def decimalToBinary(num):
    return bin(num).replace('0b', "")


def binaryToLetters(binary):
    binary_to_str = {
        "0": "zero",
        "1": "one"
    }
    str_binary = ""
    for digit in binary:
        str_binary += binary_to_str[digit]

    return str_binary

# varibles
suite, n = [int(i) for i in input().split()]

for i in range(n):
    last_number = suite
    suite_binary = decimalToBinary(suite)
    str_binary = binaryToLetters(suite_binary)
    suite = len(str_binary)

    if last_number == suite:
        break

print(suite)
