# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.


class Solution:
    def singleNonDuplicate(self, nums):
        # Get the length of the array
        n = len(nums)

        # Check if there is only one element in the array
        if n == 1:
            return nums[0]

        # Check if the non-duplicate is the first element
        if nums[0] != nums[1]:
            return nums[0]

        # Check if the non-duplicate is the last element
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        # Initialize low and high pointers for binary search
        low, high = 1, n - 2

        # Binary search loop
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2

            # Check if nums[mid] is the single non-duplicate
            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # Check which side to continue searching based on parity
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                # If mid is odd and mid-1 is equal, or if mid is even and mid+1 is equal, move to the right side
                low = mid + 1
            else:
                # Otherwise, move to the left side
                high = mid - 1

        # This line should not be reached in a valid input case
        return -1  # Placeholder value, should never be returned

solution_object = Solution()
#Test case 1
result = solution_object.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print(result)
#Test case 2
result = solution_object.singleNonDuplicate([3,3,7,7,10,11,11])
print(result)