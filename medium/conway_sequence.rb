r = []
r.push(gets.to_i)
l = gets.to_i

for i in (0...l - 1)
    j = 0
    r_temp = []
    while (j < r.length)
        find_occurence = true
        k = 1
        while (j + k < r.length - 1) && find_occurence
            if r[j] == r[j + k]
                k += 1
            else
                find_occurence = false
            end
        end
        r_temp.push(k.to_s)
        r_temp.push(r[j])
        j += k
    end
    r = r_temp
end

puts r.join(" ")


