import sys
import math
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

l = int(input())
h = int(input())
t = input()

rows = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rows_ascii = []

for i in range(h):
    row = input()
    rows.append(row)

to_ascii = [c for c in t]

for lign in range(h):
    row_ascii = ''
    for j in range(len(to_ascii)):
        char = to_ascii[j].upper()
        if alphabet.find(char) != -1:
            letter_index = alphabet.find(char)
            row_ascii += rows[lign][slice((letter_index * l),(letter_index * l + l), 1)]
        else:
            interrogation_index = len(rows[lign])
            row_ascii += rows[lign][slice((interrogation_index) - l,(interrogation_index), 1)]

    rows_ascii.append(row_ascii)

for row_ascii in rows_ascii:
    row_ascii += "\n"

response = "\n".join(rows_ascii)

print(response)