# Reverse an array but skip even numbers

nums = [1,4,9,7,6,100,201,145,150,189,164,406,175,133]
print("Original Array - ", nums)

left = 0
right = len(nums)-1

while left < right:
    if nums[left] % 2 == 0:
        left+=1
        continue
    if nums[right] % 2 == 0:
        right-=1
        continue
    nums[left], nums[right] = nums[right], nums[left]
    left, right = left+1, right-1
print("Reversed Array - ", nums)