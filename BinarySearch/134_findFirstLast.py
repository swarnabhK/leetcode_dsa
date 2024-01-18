# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]


class Solution:
    def first_position(self, nums, target):
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1
        # Initialize variable to store the first position (default to -1)
        first = -1

        # Binary search loop
        while left <= right:
            # Calculate mid index
            mid = (left + right) // 2

            # Check if target is found at mid
            if nums[mid] == target:
                # Update first and move right pointer to search for earlier occurrences
                first = mid
                right = mid - 1
            elif target > nums[mid]:
                # If target is greater, search in the right half
                left = mid + 1
            else:
                # If target is smaller, search in the left half
                right = mid - 1

        # Return the first position
        return first

    def last_position(self, nums, target):
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1
        # Initialize variable to store the last position (default to -1)
        last = -1

        # Binary search loop
        while left <= right:
            # Calculate mid index
            mid = (left + right) // 2

            # Check if target is found at mid
            if nums[mid] == target:
                # Update last and move left pointer to search for later occurrences
                last = mid
                left = mid + 1
            elif target < nums[mid]:
                # If target is smaller, search in the left half
                right = mid - 1
            else:
                # If target is greater, search in the right half
                left = mid + 1

        # Return the last position
        return last

    def searchRange(self, nums, target):
        # Call first_position to find the first occurrence
        first = self.first_position(nums, target)

        # If first position is not found, return [-1, -1]
        if first == -1:
            return [-1, -1]

        # Call last_position to find the last occurrence
        last = self.last_position(nums, target)

        # Return the result as a list [first, last]
        return [first, last]


# Create an object of the Solution class
solution_object = Solution()

# Example usage: Call the searchRange method
result = solution_object.searchRange([5, 7, 7, 8, 8, 10], 8)

# Print the result
print(result)
