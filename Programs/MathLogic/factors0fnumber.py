#Print all factors of a given number

def factors_num(num):
    result = []
    
    for i in range(1,(num//2) + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

num = int(input("Enter a number - "))
print("The factors of a given number are - ", factors_num(num))
