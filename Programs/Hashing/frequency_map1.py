num = [0,3,5,6,1,5,2,18,36,1,1,5]
frequency_map = dict()

for n in num:
    if n in frequency_map:
        frequency_map[n]+= 1
    else:
        frequency_map[n] = 1

print(frequency_map)

    