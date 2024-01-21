#find all the permutations of an array
#example [1,2,3]: [{1,2,3},{1,3,2},{2,1,3},{2,3,1},{3,1,2},{3,2,1}]

#start at index and check how many of the remainig indexes you can pick, keep track of the visited indexes.

def find(arr, n, ls, visited):
    if len(arr) == n:
        res.append(arr[:])
        return
    for i in range(n):
        if i not in visited:
            arr.append(ls[i])
            visited.add(i)
            find(arr, n, ls, visited)
            arr.pop()
            visited.remove(i)


res = []
l = [1, 2, 3, 4]
find([], len(l), l, set())
print(res)

