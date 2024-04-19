import sys
import math

def split_by_n(word, l):
    while word:
        size = l.pop(0)
        yield word[:size]
        word = word[size:]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

phrase = input()

size_reversed = [len(x) for x in phrase.split()][::-1]

phrase_merge = ''.join(phrase.split())

letter = ""
position_array = []
for i in range(len(phrase_merge)):
    if (alphabet.index(phrase_merge[i])+1) % 4 == 0:
        letter += phrase_merge[i]
        position_array.append(i)

if len(position_array) > 0:
    letters_shifted = letter[-1] + letter[:-1]

print(phrase_merge, file=sys.stderr)
for j in range(len(position_array)):
    phrase_merge = phrase_merge[:position_array[j]] + letters_shifted[j] + phrase_merge[position_array[j]+1:]

print("### Phase 2 ###", file=sys.stderr)

letter = ""
position_array = []
for k in range(len(phrase_merge)):
    if (alphabet.index(phrase_merge[k])+1) % 3 == 0:
        letter += phrase_merge[k]
        position_array.append(k)

letters_shifted = letter[1:] + letter[0]

for l in range(len(position_array)):
    phrase_merge = phrase_merge[:position_array[l]] + letters_shifted[l] + phrase_merge[position_array[l]+1:]

letter = ""
position_array = []
for m in range(len(phrase_merge)):
    if (alphabet.index(phrase_merge[m])) % 2 == 1:
        letter += phrase_merge[m]
        position_array.append(m)
        
letters_reversed = letter[::-1]

for n in range(len(position_array)):
    phrase_merge = phrase_merge[:position_array[n]] + letters_reversed[n] + phrase_merge[position_array[n]+1:]

# Splitting
phrase_stage_4 = " ".join(list(split_by_n(phrase_merge, size_reversed)))
print(phrase_stage_4)

