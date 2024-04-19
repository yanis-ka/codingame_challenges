# Variables
n = gets.to_i
best_t_seconds = 0
best_t = ""
i = 0
n.times do
  t = gets.chomp
  t_seconds = t.split(':')
  t_seconds = ((t_seconds[0]).to_i * 3600) + ((t_seconds[1]).to_i * 60) + (t_seconds[2]).to_i
  if i == 0 or t_seconds < best_t_seconds
      best_t_seconds = t_seconds
      best_t = t
  end
  i += 1
end
puts best_t
