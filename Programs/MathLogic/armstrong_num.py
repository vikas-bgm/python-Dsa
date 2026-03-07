# Armstrong numberr

def armstrong(n):
    num = n
    total = 0
    digits = len(str(num))
    while num > 0:
        last_digit = num % 10
        total = total + (last_digit ** digits)
        num = num // 10
    return total

num = int(input("Enter the number - "))
if num == armstrong(num):
    print("The num is armstrong number ")
else:
    print("Not armstrong number")