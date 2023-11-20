from collections import defaultdict

def largestUniqueNumber(nums):
    # find occurence of each integer
    counts = defaultdict(int)
    largest = -1
    for num in nums:
        counts[num]+=1
    for key in counts:
        if(counts[key]==1 and key>largest):
            largest = key
    return largest
            

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(largestUniqueNumber([9,9,8,8]))