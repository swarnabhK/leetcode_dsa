def pivotIndex(nums):
    windowSum = 0
    P_sum =  [0]*len(nums)
    for i in range(len(nums)):
        windowSum+=nums[i]
        P_sum[i] = windowSum
    for i in range(len(nums)):
        if(i!=0):
            left = P_sum[i-1]
        else:
            left = 0
        right = P_sum[len(nums)-1] - P_sum[i]
        if(left==right):
            return i
    return -1


print(pivotIndex([1,7,3,6,5,6]))