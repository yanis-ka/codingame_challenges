import sys
import math

# Functions
def get(x=0, y=0):
    global food
    global w
    global h
    global visited
    have = visited.get((x,y), False)
    if have:
        return have
    current = food[y][x]
    if x + 1 >= w:
        right = 0
    else:
        right = get(x + 1, y)
    if y + 1 >= h:
        down = 0
    else:
        down = get(x, y + 1)
    current += (right, down)[down > right]
    visited[(x,y)] = current
    return current


# Variables
visited = {}
food = []
w, h = [int(i) for i in input().split()]

for i in range(h):
    food.append([])
    for j in input().split():
        food[i].append(int(j))
print(get())