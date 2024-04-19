l = gets.to_i
h = gets.to_i
t = gets.chomp

rows = []
response = ""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

h.times do
  row = gets.chomp
  rows.push(row)
end

to_ascii = t.split('')

rows_ascii = []

for i in 0...h
    row_ascii = ""
    to_ascii.each do |char|
        # test_char = char.match?('[a-zA-Z]').to_s
        char = char.upcase
        test_char = alphabet.include?(char)
        if test_char
            char = char.upcase
            letter_index = alphabet.index(char)
            row_ascii += rows[i].slice((letter_index * l)...(letter_index * l + l))
        else
            # STDERR.puts "in the else"
            interrogation_index = rows[i].length
            row_ascii += rows[i].slice((interrogation_index - l)...(interrogation_index))
        end
    end
    rows_ascii.push(row_ascii)
end
response = rows_ascii.join("\n")
puts response
