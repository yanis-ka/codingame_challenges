import sys
import math

p = []
n = int(input())
for i in range(n):
    pi = int(input())
    p.append(pi)

ds = []
p.sort()

for i in range(0, len(p) - 1, 1):
    d = p[i + 1] - p[i]
    ds.append(d)

print(min(ds))
