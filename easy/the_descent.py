import sys
import math

# game loop
while True:
    heights = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        heights.append(mountain_h)

    destroy = heights.index(max(heights))
    print(destroy)
