# Reverse an array using while loop 

nums = [1,2,5,6,11,10,20,35]
print("Original list - ",nums)
left=0
right=len(nums)-1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left, right = left+1, right-1
print("Reversed list - ", nums)