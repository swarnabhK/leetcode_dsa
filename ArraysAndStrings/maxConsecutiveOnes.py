def longestOnes(nums, k):
        left = right = curr = ans = 0
        for right in range(len(nums)):
            if(nums[right]==0):
                curr+=1
            while(curr>k):
                if(nums[left]==0):
                    curr-=1
                left+=1
            ans = max(right-left+1,ans)
        return ans

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)) 