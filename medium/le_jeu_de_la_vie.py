import sys
import math

# Functions
def count(r, c):
    global map1
    global width
    global height
    array = [
        [-1, -1], [-1, 0], [-1, 1],
        [ 0, -1],          [ 0, 1],
        [ 1, -1], [ 1, 0], [1, 1]]
    count = 0
    for item in array:
        rn = item[0] + r
        cn = item[1] + c
        if rn >= 0 and cn >= 0 and rn < height and cn < width:
            print(rn, cn, map1[rn][cn], file=sys.stderr)
            if map1[rn][cn] == '1':
                count += 1
    return count


# Variables
width, height = [int(i) for i in input().split()]
map1 = []
map2 = []

for i in range(height):
    line = input()
    map1.append(list(line))
for r in range(height):
    map2.append([])
    for c in range(width):
        cnt = count(r, c)
        if map1[r][c] == '1':
            if cnt < 2 or cnt > 3:
                map2[r].append('0')
            else:
                map2[r].append('1')
        else:
            if cnt == 3:
                map2[r].append('1')
            else:
                map2[r].append('0')
    print("".join(map2[r]))

print(map2, file=sys.stderr)
