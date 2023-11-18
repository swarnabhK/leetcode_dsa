def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left,right = 0, len(s)-1
    
    while(left<right):
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1


#local tests
s = ["h","e","l","l","o"]
print("Before reversing: ",s)
reverseString(s)
print("After reversing: ",s)