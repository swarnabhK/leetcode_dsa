
def minSubArrayLen(target, nums):
    left = right = s = 0
    ans = float('inf')
    for right in range(len(nums)):
        s+= nums[right]
        while(s>=target):
            ans = min(ans,right-left+1)
            s  = s - nums[left]
            left+=1
    return ans if ans!=float('inf') else 0
        

print(minSubArrayLen(7,[2,3,1,2,4,3]))