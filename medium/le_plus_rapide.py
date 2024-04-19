import sys
import math

# variable
n = int(input())
best_t_seconds = 0
best_t = ""
for i in range(n):
    t = input()

    # convert t in seconds
    t_seconds = t.split(':')
    t_seconds = (int(t_seconds[0]) * 3600) + (int(t_seconds[1]) * 60) + int(t_seconds[2])

    if i == 0 or t_seconds < best_t_seconds:
        best_t_seconds = t_seconds
        best_t = t

print(best_t)
