from collections import defaultdict
def areOccurrencesEqual(s):
    counts = defaultdict(int)
    for c in s:
        counts[c]+=1
    freqs = counts.values()
    return len(set(freqs))==1     

print(areOccurrencesEqual("abacbc"))
print(areOccurrencesEqual("aaabb"))