def sortedSquares(nums):
    n = len(nums)
    result = [0]*n
    left,right = 0,n-1
    for i in range(n-1,-1,-1):
        if(abs(nums[left])>abs(nums[right])):
            result[i] = nums[left]*nums[left]
            left+=1
        else:
            result[i] = nums[right]*nums[right]
            right-=1
    return result


print(sortedSquares([-4,-1,0,3,10]))