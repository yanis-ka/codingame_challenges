import sys
import math

r = []
r.append(input())
l = int(input())

for i in range(l - 1):
    j = 0
    r_temp = []

    # Running througth r
    while(j < len(r)):
        find_occurence = True
        k = 1

        # number of occurences in r
        while(j + k < len(r)) and find_occurence:
            if r[j] == r[j + k]:
                k += 1
            else:
                find_occurence = False

        # reconstruction of the Conway sequence
        r_temp.append(str(k))
        r_temp.append(r[j])
        j += k
    
    r = r_temp
    print(' '.join(r))


print(' '.join(r))
