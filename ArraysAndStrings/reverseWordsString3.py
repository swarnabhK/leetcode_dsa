def reverseWords(s):
  begin = 0
  s = list(s)
  n = len(s)
  for i in range(n):
      if(s[i]==' ' or i==n-1):
          left = begin
          right = i if i==n-1 else i-1
          begin= i+1
          while(left<right):
              s[left],s[right] = s[right],s[left]
              left+=1
              right-=1
  return "".join(s)

print(reverseWords("Let's take LeetCode contest"))