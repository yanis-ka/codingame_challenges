import sys
import math

N = int (input())
numbers = set()
for i in range(N):
    number = input()
    for i in range(1, len(number)+1):
        numbers.add(number[:i])
print(len(numbers))
