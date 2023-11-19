def reversePrefix(word, ch):
    right = word.find(ch)
    if(right==-1):
        return word
    left = 0
    word = list(word)
    while(left<right):
        word[left],word[right] = word[right],word[left]
        left+=1
        right-=1
    return "".join(word)

print(reversePrefix("abcdefd","d"))