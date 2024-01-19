#Find the number of subsequences with the sum k
# just need to keep track of the sum at each pick and not pick condition.
# find the value returned by each tree for a function call , and give the sum back. 


def find(ind,n,l,s,target):
    if(ind==n):
        if(s==target):
            return 1
        return 0
    #pick condiiton
    s+=l[ind]
    lt = find(ind+1,n,l,s,target)
    s-=l[ind]
    rt = find(ind+1,n,l,s,target)
    return lt+rt


ls  = [1,2,2,1]
print(find(0,len(ls),ls,0,3))
ls = [1,2,1]
print(find(0,len(ls),ls,0,2))
