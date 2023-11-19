def equalSubstring(s, t, maxCost):
    #can s[i] be turned into b[i]?
    left = right = diff = ans = 0
    for right in range(len(s)):
        diff+= abs(ord(s[right])-ord(t[right]))
        while(diff>maxCost):
            diff = diff - abs(ord(s[left])-ord(t[left]))
            left+=1
        ans = max(ans,right-left+1)
    return ans

print(equalSubstring("abcd","bcdf",3))