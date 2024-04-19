import sys
import math

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevator_positions = []
ways_up = []

for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevator_position = { "floor": elevator_floor, "position": elevator_pos }
    elevator_positions.append(elevator_position)

for elevator_position in elevator_positions:
    ways_up.append(elevator_position)

ways_up.append({ 'floor': exit_floor, 'position': exit_pos })
ways_up = sorted(ways_up, key = lambda way_up : way_up['floor'])

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    for way_up in ways_up:
        if clone_floor == way_up['floor']:
            pos_stop = { 'floor': way_up['floor'], 'position': way_up['position'] }

    if clone_floor == pos_stop['floor']:
        if clone_pos < pos_stop['position'] and direction == "LEFT":
            print("BLOCK")
        elif clone_pos > pos_stop["position"] and direction == "RIGHT":
            print("BLOCK")
        else:
            print("WAIT")
    else:
        print("WAIT")
