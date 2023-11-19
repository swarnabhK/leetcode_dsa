def getAverages(nums, k):
        n = len(nums)
        sub_len = 2*k+1
        avg = [-1]*n
        prefix = [nums[0]]
        if(sub_len>n):
            return avg
        for i in range(1,len(nums)):
             prefix.append(nums[i]+prefix[-1])
        print(prefix)
        for i in range(k,n-k):
            sum_s = prefix[i+k] - prefix[i-k] + nums[i-k]
            avg[i] = sum_s//sub_len
        print(avg)

getAverages([40527,53696,10730,66491,62141,83909,78635,18560],2)