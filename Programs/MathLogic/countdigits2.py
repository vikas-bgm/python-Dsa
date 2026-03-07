# another way to count the no of digits

from math import *

def count(num):
    return(int(log10(num)+1))

num = int(input("Enter the number - "))
print("The count is - ", count(num))