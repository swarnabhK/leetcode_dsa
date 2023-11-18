def waysToSplitArray(nums):
    prefix,count = [nums[0]],0
    for i in range(1,len(nums)):
        prefix.append(nums[i]+prefix[-1])
    for i in range(len(nums)-1):
        sum_left = prefix[i]
        sum_right = prefix[-1] - prefix[i]
        if(sum_left>=sum_right):
            count+=1
    return count


#local tests

print(waysToSplitArray([10,4,-8,7]))
print(waysToSplitArray([2,3,1,0]))