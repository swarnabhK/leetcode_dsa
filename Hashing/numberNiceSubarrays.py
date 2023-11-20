from collections import defaultdict


def numberOfSubarrays(nums, k):
    # Initialize the hashmap with the number of current odd numbers
    # If current - k exists in the map, that means there is a subarray
    # that has k number of odd numbers ending at the current index (iteration)
    map_odd_count = defaultdict(int)
    map_odd_count[0] = 1  # Initialize with 0 odd numbers (an empty subarray)

    curr = no_subarrays = 0  # Initialize the current odd number count and the total count of subarrays

    for num in nums:
        if num % 2 == 1:  # Check if the current number is odd
            curr += 1  # Increment the count of current odd numbers

        diff = curr - k  # If diff is in the map, it means there is a subarray with k odd numbers
        if diff in map_odd_count:
            no_subarrays += map_odd_count[diff]

        map_odd_count[curr] += 1  # Update the map with the current odd number count

    return no_subarrays

print(numberOfSubarrays([1,1,2,1,1],3))
print(numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2))