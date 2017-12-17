my_list = [4,2,4,0,2,4,5,7,8,9,23,8,5,4,2,2,34,4,45]
maximum = 0
for x in my_list:
    if x>maximum:
        maximum = x
print(maximum)

minimum = maximum
for y in my_list:
    if y<minimum:
        minimum = y
print(minimum)
