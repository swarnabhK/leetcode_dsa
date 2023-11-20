from collections import defaultdict
def findWinners(matches):
    losers = defaultdict(int)
    for match in matches:
        if(match[0] not in losers):
            losers[match[0]] = 0
        losers[match[1]]+=1
    result = [sorted([key for key in losers if losers[key]==0]), sorted([key for key in losers if losers[key]==1])]
    
    return result
            

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(findWinners([[2,3],[1,3],[5,4],[6,4]]))