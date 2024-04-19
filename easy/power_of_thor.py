import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_x = initial_tx
thor_y = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    direction_x = ""
    direction_y = ""

    if thor_x > light_x:
        direction_x = "W"
        thor_x -= 1
    elif thor_x < light_x: 
        direction_x = "E"
        thor_x += 1

    if thor_y > light_y:
        direction_y = "N"
        thor_y -= 1
    elif thor_y < light_y: 
        direction_y = "S"
        thor_y += 1

    print(direction_y + direction_x)
