STDOUT.sync = true # DO NOT REMOVE
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = gets.split(" ").collect { |x|
 x.to_i
}

elevator_positions = []

nb_elevators.times do
  elevator_floor, elevator_pos = gets.split(" ").collect { |x| x.to_i }
  elevator_position = { floor: elevator_floor,
                        position: elevator_pos }
  elevator_positions.push(elevator_position)
end

ways_up = []
ways_up = elevator_positions.map(&:itself)
ways_up.push({ floor: exit_floor, position: exit_pos })
ways_up.sort_by! { |way_up| way_up[:floor] }

# game loop
loop do
    clone_floor, clone_pos, direction = gets.split(" ")
    clone_floor = clone_floor.to_i
    clone_pos = clone_pos.to_i

    pos_stops = ways_up.select { |way_up| way_up[:floor] == clone_floor }
    pos_stop = pos_stops.first
    if pos_stop
        if clone_floor == pos_stop[:floor]
            if clone_pos < pos_stop[:position] && direction == 'LEFT'
                puts "BLOCK"
            elsif clone_pos > pos_stop[:position] && direction == 'RIGHT'
                puts "BLOCK"
            else
                puts "WAIT"
            end
        else
            puts "WAIT"
        end
    else
        puts "WAIT"
    end
end

