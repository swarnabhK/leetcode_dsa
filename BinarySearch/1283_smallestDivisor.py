# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
# The test cases are generated so that there will be an answer.
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

from math import ceil

class Solution:
    def findSum(self, nums, threshold, k):
        # Function to check if the sum of ceil(nums[i]/k) for all nums[i] is less than or equal to threshold
        s = 0
        for num in nums:
            s += ceil(num / k)
        return s <= threshold

    def smallestDivisor(self, nums, threshold):
        # Initialize low and high pointers for binary search based on nums
        low, high = 1, max(nums)
        # Initialize variable to store the result (smallest divisor)
        ans = 1

        # Binary search loop
        while low <= high:
            # Calculate mid value for divisor
            mid = (low + high) // 2

            # Check if the sum of ceil(nums[i]/mid) for all nums[i] is less than or equal to threshold
            if self.findSum(nums, threshold, mid):
                # If possible, update ans to mid and search in the left half
                high = mid - 1
                ans = mid
            else:
                # If not possible, search in the right half
                low = mid + 1

        # Return the smallest divisor that satisfies the threshold condition
        return ans


solution_object = Solution()
#Test case 1
result = solution_object.smallestDivisor([1,2,5,9],6)
print(result)
#Test case 2
result = solution_object.smallestDivisor([44,22,33,11,1],5)
print(result)