#find all the subsequences of an array that sum to a value k
#example arr = [1,2,1], k=2. The subsequences are: [1,1],[2]

def sumSubsequencesK(l):
    res = []
    def find(arr,ls,ind,n,s,k):
        if(s==k):
            res.append(arr.copy())
            return
        if(ind==n):
            return
        s+=ls[ind]
        arr.append(ls[ind])
        find(arr,ls,ind+1,n,s,k)
        s-=ls[ind]
        arr.pop()
        find(arr,ls,ind+1,n,s,k)
    find([],l,0,len(l),0,2)
    return res


print(sumSubsequencesK([1,2,1]))
