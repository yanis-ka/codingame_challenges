import sys
import math

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print("0")

positives = []
negatives = []
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    negatives.append(t) if t < 0 else positives.append(t)

if len(positives) == 0:
    print(max(negatives))
elif len(negatives) == 0:
    print(min(positives))
elif (min(positives) + max(negatives) > 0):
    print(max(negatives))
else:
    print(min(positives))
