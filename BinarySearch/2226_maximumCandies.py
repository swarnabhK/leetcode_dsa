# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.
# You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.
# Return the maximum number of candies each child can get.
# Input: candies = [5,8,6], k = 3
# Output: 5
# Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

class Solution:
    def bagCandies(self, candies, b):
        # Function to calculate the total number of bags that can be formed with a given bag size (b)
        bags = 0
        for c in candies:
            bags += c // b
        return bags

    def maximumCandies(self, candies, k) -> int:
        # Initialize low and high pointers for binary search based on candies
        low, high = 1, max(candies)
        # Initialize variable to store the result (maximum bag size)
        ans = 0

        # Binary search loop
        while low <= high:
            # Calculate mid value for bag size
            mid = (low + high) // 2

            # Check the total number of bags that can be formed with mid bag size
            bags = self.bagCandies(candies, mid)

            # Adjust the pointers based on the comparison with k
            if bags >= k:
                # If total bags with mid bag size is greater or equal to k, search in the right half
                low = mid + 1
                ans = mid
            else:
                # If total bags with mid bag size is less than k, search in the left half
                high = mid - 1

        # Return the maximum bag size required to achieve the given number of bags (k)
        return ans


solution_object = Solution()
#Test case 1
result = solution_object.maximumCandies([5,8,6],3)
print(result)
#Test case 2
result = solution_object.maximumCandies([2,5],11)
print(result)