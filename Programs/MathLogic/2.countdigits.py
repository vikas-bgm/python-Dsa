#Count the no digits in an integer

def count_digit(n):
    num = n
    count = 0
    while num > 0:
        count+=1
        num = num//10
    return count

n = int(input("Enter the number - "))
#count_digit(n)
print("The count is -", count_digit(n))