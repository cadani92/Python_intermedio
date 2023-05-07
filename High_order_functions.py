# Uso filter

#my_list = [1, 2, 4, 5, 6, 7, 8, 12, 13, 15, 17, 19, 20, 21, 22]

#odd = list(filter(lambda x: x%2 != 0, my_list))

#print(odd)

# Uso map

#my_list = [1, 2, 3, 4, 5]

#square = list(map(lambda x: x**2, my_list))

#print(square)

#Uso reduce

from functools import reduce

my_list = [2, 2, 2, 2, 2]

all_multiplied = reduce(lambda a, b: a*b, my_list)

print(all_multiplied)