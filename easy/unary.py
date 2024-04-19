import sys
import math

binary = ''
message = input()

for i in range(len(message)):
    char_in_binary = str(bin(ord(message[i])))[2:]
    char_in_binary = char_in_binary.zfill(7)

    binary += char_in_binary

last_char = ' '
coded_message = ''
encoded_bits = [' 00 0', ' 0 0']

for i in range(len(binary)):
    if binary[i] != last_char:
        last_char = binary[i]
        coded_message += encoded_bits[ord(last_char) - ord('0')]
    else:
        coded_message += '0'

print(coded_message[1:])
