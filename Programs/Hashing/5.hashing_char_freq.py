# Character hashing with dictonaries

chars = "Hello Worldw"

hash_map= dict()

for char in chars:
    hash_map[char] = hash_map.get(char,0) +1
print(hash_map)