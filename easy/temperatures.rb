n = gets.to_i # the number of temperatures to analyse
if n == 0
    puts "0"
end
inputs = gets.split(" ")
positives = []
negatives = []
for i in 0..(n-1)
  # t: a temperature expressed as an integer ranging from -273 to 5526
  t = inputs[i].to_i
  t < 0 ? negatives << t : positives << t
end

if (positives.empty?)
    puts "#{negatives.max}"
elsif (negatives.empty?)
    puts "#{positives.min}"
elsif ((positives.min + negatives.max) > 0)
    puts "#{negatives.max}"
else
    puts "#{positives.min}"
end
