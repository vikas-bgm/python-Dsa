# Frequency map in dictionary

num = [1,3,5,6,1,5,2,18,36,18,5,3,100]
frequency_map = dict()

for i in range(0,len(num)):
    if num[i] in frequency_map:
        frequency_map[num[i]]+=1
    else:
        frequency_map[num[i]] = 1
print(frequency_map)