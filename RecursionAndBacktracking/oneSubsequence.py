def find(ind, arr, n, ls, target, s):
    if ind == n:
        if s == target:
            print(arr)
            return True
        return False

    # pick condition
    s += ls[ind]
    arr.append(ls[ind])
    if find(ind + 1, arr, n, ls, target, s):
        return True

    # undo the pick
    s -= ls[ind]
    arr.pop()
    # not pick condition
    if find(ind + 1, arr, n, ls, target, s):
        return True
    return False

l = [1, 2, 1]
find(0, [], len(l), l, 2, 0)
