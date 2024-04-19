import sys
import math
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x = x0
y = y0

x_min = -1
x_max = w
y_min = -1
y_max = h

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if bomb_dir.__contains__('R'):
        x_min = x
        x += round((x_max - x_min)/2)
    elif bomb_dir.__contains__('L'):
        x_max = x
        x -= round((x_max - x_min)/2)

    if bomb_dir.__contains__('D'):
        y_min = y
        y += round((y_max - y_min)/2)
    elif bomb_dir.__contains__('U'):
        y_max = y
        y -= round((y_max - y_min)/2)

    if x == 1 and bomb_dir.__contains__('L'):
        x = 0

    if y == 1 and bomb_dir.__contains__('U'):
        y = 0

    print("{} {}".format(x, y))
