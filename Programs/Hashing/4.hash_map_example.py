# Generic way of hashing in dictonary

nums = [1,3,4,1,2,3,10,3,10,4,3,1,2]

hash_map= dict()

for x in nums:
    hash_map[x] = hash_map.get(x,0) +1
print(hash_map)