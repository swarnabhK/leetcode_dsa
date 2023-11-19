def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    slow = 0
    for fast in range(len(nums)):
        if(nums[fast]!=0):
            nums[slow] = nums[fast]
            slow+=1
    while(slow<len(nums)):
        nums[slow] = 0
        slow+=1

nums = [0,1,0,3,12]
print(nums)
moveZeroes(nums)
print(nums)