# Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each # query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise

# For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the # subarray sums are [12, 14, 12].


def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    # Build a prefix sum array
    for i in range(1,len(nums)):
        prefix.append(nums[i]+prefix[-1])
    bool_array = []
    s = []
    for q in queries:
        subarray_sum = prefix[q[1]] - prefix[q[0]]+nums[q[0]]
        bool_array.append(subarray_sum<limit)
    return bool_array


#local tests
print("The bool array is: ",end="")
print(answer_queries([1, 6, 3, 2, 7, 2],[[0, 3], [2, 5], [2, 4]],13))