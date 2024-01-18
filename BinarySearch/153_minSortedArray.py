# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.


class Solution:
    def findMin(self, nums):
        # Initialize low and high pointers for binary search
        low, high = 0, len(nums) - 1
        # Initialize a variable to store the minimum element (initially set to positive infinity)
        minimum = float("inf")

        # Binary search loop
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2

            # Update the minimum element with the minimum of the current minimum and nums[mid]
            minimum = min(minimum, nums[mid])

            # Check if the array is rotated on the right side of mid
            if nums[mid] > nums[high]:
                # If yes, search in the right half
                low = mid + 1
            else:
                # If not, search in the left half
                high = mid - 1

        # Return the minimum element found during the binary search
        return minimum


solution_object = Solution()
#Test case 1
result = solution_object.findMin([3,4,5,1,2])
print(result)
#Test case 2
result = solution_object.findMin([4,5,6,7,0,1,2])
print(result)