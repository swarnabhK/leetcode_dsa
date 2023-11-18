
def findMaxAverage(nums,k):
    s = ans = avg = 0
    for i in range(k):
        s+=nums[i]
    ans = s/k
    for i in range(k,len(nums)):
        s+=nums[i]-nums[i-k]
        avg = s/k
        ans = max(ans,avg)
    return ans


print(findMaxAverage([1,12,-5,-6,50,3],4))

