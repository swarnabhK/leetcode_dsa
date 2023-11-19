def reverseOnlyLetters(s):
  left,right = 0,len(s)-1
  s = list(s)
  while(left<right):
      if(not s[left].isalpha()):
          left+=1
      elif(not s[right].isalpha()):
          right-=1
      elif(s[left].isalpha() and s[right].isalpha()):
          s[left],s[right] = s[right],s[left]
          left+=1
          right-=1
  return "".join(s)
  

print(reverseOnlyLetters("a-bC-dEf-ghIj"))
  