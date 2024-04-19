vs = []
diffs = []

n = gets.to_i
inputs = gets.split
for i in 0..(n-1)
  v = inputs[i].to_i
  vs.push(v)
end
vs.each_with_index do |v, index|
  v_to_compare = vs[index...vs.length]
  diff = v_to_compare.min - v
  diffs.push(diff)
end

p = diffs.min
p >= 0 ? 0 : p
puts p
