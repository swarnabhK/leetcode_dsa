def findMiddleIndex(nums):
    if(len(nums)==1):
        return 0
    prefix = [nums[0]]
    for i in range(1,len(nums)):
        prefix.append(nums[i]+prefix[-1])
    for i in range(len(prefix)):
        if(i==0):
            left_sum = 0
        else:
            left_sum = prefix[i-1]
        right_sum = prefix[-1] - prefix[i]
        if(right_sum==left_sum):
            return i
    return -1


#local tests

print(findMiddleIndex([2,3,-1,8,4]))