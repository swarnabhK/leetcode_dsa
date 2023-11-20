from collections import defaultdict
def subarraySum(nums, k):
    # First initialize the hashmap to keep track of the current prefix sum
    # An empty array has a sum of 0 which appears once
    prefix_map = defaultdict(int)
    prefix_map[0] = 1
    curr = no_subarrays = 0

    for num in nums:
        curr += num  # Variable to track the current prefix sum at this iteration
        diff = curr - k  # If curr - k exists in the hashmap, there is a subarray with sum k

        # The condition below means there exists a subarray with sum k from some previous index
        # to the current index. This is because curr - prefix_sum = k, where prefix_sum is the sum
        # of elements from some previous index to the current index.
        if diff in prefix_map:
            no_subarrays += prefix_map[diff]

        # Update the prefix_map with the current prefix sum
        prefix_map[curr] += 1

    return no_subarrays

print(subarraySum([1,1,1],2))
print(subarraySum([1,-1,0],0))