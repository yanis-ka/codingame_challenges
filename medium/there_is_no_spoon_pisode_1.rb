STDOUT.sync = true # DO NOT REMOVE
# Don't let the machines win. You are humanity's last hope...
lines = []

width = gets.to_i # the number of cells on the X axis
height = gets.to_i # the number of cells on the Y axis
height.times do
  line = gets.chomp # width characters, each either 0 or .
  lines.push(line)
end

# Write an action using puts
# To debug: STDERR.puts "Debug messages..."

nodes = []

lines.each_with_index do |line, index|
  line.split('').each_with_index do |char, id|
    if char == "0"
      noeud = { x: id,
                y: index }
      nodes.push(noeud)
    end
  end
end

colomn = []

if nodes.length > 1
  for i in 0...height
      bottom_nodes = nodes.select do |colomn_node|
          colomn_node[:x] == nodes[i][:x] && colomn_node[:y] > nodes[i][:y]
          colomn.push(colomn_node)
      end
  end
end
colomn = colomn.uniq

nodes.each_with_index do |node, index|
    if node[:x] != nodes.last[:x] || node[:y] != nodes.last[:y]

        right_node = node[:y] == nodes[index + 1][:y] ?
        { x: nodes[index + 1][:x], y: nodes[index + 1][:y] } : { x: "-1", y: "-1" }
        bottom_nodes = []
        bottom_nodes = nodes.select do |colomn_node|
            colomn_node[:x] == node[:x] && colomn_node[:y] > node[:y]
        end

        bottom_node = !bottom_nodes.empty? ? { x: bottom_nodes.first[:x], y: bottom_nodes.first[:y] } : { x: "-1", y: "-1" }

    else
        right_node = { x: "-1", y: "-1" }
        bottom_node = { x: "-1", y: "-1" }
    end
    puts "#{node[:x]} #{node[:y]} #{right_node[:x]} #{right_node[:y]} #{bottom_node[:x]} #{bottom_node[:y]}"
end

# Three coordinates: a node, its right neighbor, its bottom neighbor
# puts "0 0 1 0 0 1"