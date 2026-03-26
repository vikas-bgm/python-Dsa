#Reverse an array using Recursion

nums = [1,3,6,10,34,56,18,80,100,203,146,36,10]

def func(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left+1, right-1)

#func(nums,0,len(nums)-1)            # Reverses the whole list/array
func(nums, 3, 9)                     # Reverses only the specifird indexes from 3 to 9
print(nums)