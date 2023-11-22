from collections import defaultdict
def maxNumberOfBalloons(text):
    counts = defaultdict(int)
    for c in text:
        counts[c]+=1
    return min(counts['b'],counts['a'],counts['l']//2,counts['o']//2,counts['n']) 


print(maxNumberOfBalloons('loonbalxballpoon'))
print(maxNumberOfBalloons('nlaebolko'))