from math import sqrt

def fact_num(num):
    result = []

    for i in range(1,int(sqrt(num)+1)):
        if num % i == 0:
            result.append(i)
            if (num//i)!= i:
                result.append(num//i)
    result.sort()
    return result

num = int(input("Enter a number - "))
print(fact_num(num))       