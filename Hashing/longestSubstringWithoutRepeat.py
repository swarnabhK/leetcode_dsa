from collections import defaultdict

def lengthOfLongestSubstring(s) -> int:
    left = ans = 0
    counts = defaultdict(int)
    for right in range(len(s)):
        counts[s[right]]+=1
        while(counts[s[right]]>1):
            counts[s[left]]-=1
            left+=1
        ans = max(ans,right-left+1)
    return ans

print(lengthOfLongestSubstring("abcabcbb"))