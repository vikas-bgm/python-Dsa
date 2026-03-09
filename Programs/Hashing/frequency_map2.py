# Optimal way of frequency in dict

num = [1,3,2,1,5,10,1,3,10]

hash_map = dict()
n = len(num)

for i in range(0,n):
    hash_map[num[i]] = hash_map.get(num[i],0) + 1
print(hash_map)