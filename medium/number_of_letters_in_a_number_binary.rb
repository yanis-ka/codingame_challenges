# Functions
def binaryToLetters(binary)
    binary_to_str = { "0" => "zero", "1" => "one" }
    str_binary = ""
    binary = binary.split('')
    binary.each do |digit|
        str_binary += binary_to_str[digit]
    end
    return str_binary
end

# Variables
suite, n = gets.split.map { |x| x.to_i }

for i in 1..n
    last_number = suite
    suite_binary = suite.to_s(2)
    str_binary = binaryToLetters(suite_binary)
    suite = str_binary.length

    if last_number == suite
        break
    end
end

puts suite
