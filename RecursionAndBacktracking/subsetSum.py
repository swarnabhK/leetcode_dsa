# find the sum of all possible subsets  and return the sums in sorted order
# example : {3,1,2}: ({3},{1},{2},{3,1},{3,2},{1,2},{3,1,2},{})-> sum (0,1,2,3,3,4,5,6)
# for start with 0 index. two options, pick it not pick it . pick 3->add to sum, pick 1 add to sum, remove from sum when you are calling the other function

def find(ind,s,n,arr,ls):
    if(ind==n):
        res.append(s)
        return
    #pick condition
    s+=ls[ind]
    arr.append(ls[ind])
    find(ind+1,s,n,arr,ls)

    #not pick condition
    s-=ls[ind]
    arr.pop()
    find(ind+1,s,n,arr,ls)


res = []
l = [3,1,2]
find(0,0,len(l),[],l)
print(sorted(res))