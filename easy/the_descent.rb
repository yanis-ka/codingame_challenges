STDOUT.sync = true # DO NOT REMOVE
# game loop
loop do
  heights = []
  8.times do
    mountain_h = gets.to_i # represents the height of one mountain.
    heights << mountain_h
  end
  destroy = heights.index(heights.max)
  puts "#{destroy}"
end
