p = []
n = gets.to_i
n.times do
  pi = gets.to_i
  p.push(pi)
end
p = p.sort
ds = []
p.each_with_index do |pi, index|
    if index < p.length - 1
        d = p[index + 1] - pi
        ds.push(d)
    end
end
puts ds.min
