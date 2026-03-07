#extraction of digits/numbers in python using loops

n = int(input("Enter the number to be extracted - "))

num = n

while num > 0:
    last_digit = num % 10                               # This extracts the last digit 
    print("This is the last digit : ", last_digit)
    num = num //10                                      # This removes the last digit
    print(num)
