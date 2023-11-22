from collections import defaultdict

def groupAnagrams(strs):
    # the sorted string will be the key
    hashmap = defaultdict(list)
    for s in strs:
        st = "".join(sorted(s))
        hashmap[st].append(s)
    return hashmap.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))