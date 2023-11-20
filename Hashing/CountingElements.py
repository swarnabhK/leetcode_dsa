def countElements(arr):
    s = set(arr)
    count = 0
    for num in arr:
        if num+1 in s:
            count+=1
    return count

print(countElements([1,2,3]))
print(countElements([1,1,3,3,5,5,7,7]))