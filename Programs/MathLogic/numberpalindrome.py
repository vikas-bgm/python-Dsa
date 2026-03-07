# Check if the number is palindrom or not

# Check if the number is palindrome or not

def check_pali(num):
    n = num
    result = 0
    
    while n > 0:
        last_digit = n % 10              # extract last digit
        result = (result * 10) + last_digit
        n = n // 10

    return result


num = int(input("Enter the number - "))

if num == check_pali(num):
    print("This is Palindrome number")
else:
    print("Not Palindrome")

