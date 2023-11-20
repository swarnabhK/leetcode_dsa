from collections import defaultdict
def intersection(nums):
    counts = defaultdict(int)
    result = []
    for arr in nums:
        for num in arr:
            counts[num]+=1
    for key in counts:
        if(counts[key]==len(nums)):
            result.append(key)
    return sorted(result)

print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(intersection([[1,2,3],[4,5,6]]))