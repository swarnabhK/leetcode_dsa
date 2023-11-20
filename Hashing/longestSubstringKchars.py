#You are given a string s and an integer k. Find the length of the longest substring and the substring that contains at most k distinct characters.
#For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

from collections import defaultdict
def longestSubsDistinctK(str,k):
    left = ans = 0
    counts = defaultdict(int)
    max_right = max_left = size = 0
    for right in range(len(str)):
        counts[str[right]]+=1
        while(len(counts)>k):
            counts[str[left]]-=1
            if(counts[str[left]]==0):
                del counts[str[left]]
            left+=1
        size = right-left+1
        if(size>ans):
            ans = size
            max_right = right
            max_left = left
    return max_right,max_left,ans

str = "eceba"
right,left,size = longestSubsDistinctK(str,2)

print(str[left:right+1],size)