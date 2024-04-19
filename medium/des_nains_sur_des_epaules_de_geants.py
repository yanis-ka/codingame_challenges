import sys
import math

connection = {}

def letsCount(number):
    global connection
    max = 0
    get_array = connection.get(number, [])
    if len(get_array) == 0:
        return 0
    else:
        for item in get_array:
            temp = letsCount(item)
            if max < temp:
                max = temp
    return max + 1


n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    connection.setdefault(x, []).append(y)
max = 0
for item in connection:
    temp = letsCount(item)
    if max < temp:
        max = temp

# The number of people involved in the longest succession of influences
print(max + 1)