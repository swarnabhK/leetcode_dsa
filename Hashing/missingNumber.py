def missingNumber(nums):
    s = set(nums)
    for i in range(len(nums)+1):
        if(i not in s):
            return i


print(missingNumber([9,6,4,2,3,5,7,0,1]))