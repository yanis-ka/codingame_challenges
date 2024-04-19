STDOUT.sync = true # DO NOT REMOVE
w, h = gets.split.map { |x| x.to_i }
n = gets.to_i # maximum number of turns before game over.
x0, y0 = gets.split.map { |x| x.to_i }

x, y = x0, y0
x_min, x_max = -1, w
y_min, y_max = -1, h

# game loop
loop do
    bomb_dir = gets.chomp # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if x == 1 and bomb_dir.include?('L')
        x = 0
    elsif y == 1 and bomb_dir.include?('U')
        y = 0
    end
    if bomb_dir.include?('R')
        x_min = x
        x += ((x_max.to_f - x_min.to_f)/2).floor
    elsif bomb_dir.include?('L')
        x_max = x
        x -= ((x_max.to_f - x_min.to_f)/2).floor
    end
    if bomb_dir.include?('D')
        y_min = y
        y += ((y_max.to_f - y_min.to_f)/2).floor
    elsif bomb_dir.include?('U')
        y_max = y
        y -= ((y_max.to_f - y_min.to_f)/2).floor
    end
    puts "#{x} #{y}"
end
