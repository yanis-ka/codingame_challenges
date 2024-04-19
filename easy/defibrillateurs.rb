# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
defibs = []
positions = []
addresses = []
distances = []
lon = gets.chomp
lat = gets.chomp
lon[','] = '.'
lat[','] = '.'
n = gets.to_i
n.times do
  defib = gets.chomp
  defibs.push(defib)
end

defibs.each do |defib|
  address = defib.split(';')
  addresses.push(address)
end
addresses.each do |address|
  address[-2][','] = "."
  address[-1][','] = "."
  position = {
    lon: address[-2].to_f,
    lat: address[-1].to_f
  }
  positions.push(position)
end

positions.each do |position|
  x = (position[:lon] - lon.to_f) * (Math.cos((position[:lat] + lat.to_f) / 2))
  y = position[:lat] - lat.to_f
  d = Math.sqrt((x**2) + (y**2)) * 6371
  distances.push(d)
end

response = addresses[distances.find_index(distances.min())][1]
puts response
