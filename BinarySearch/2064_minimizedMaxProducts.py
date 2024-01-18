# You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.
# You need to distribute all products to the retail stores following these rules:
#     A store can only be given at most one product type but can be given any amount of it.
#     After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
# Return the minimum possible x.
# Input: n = 6, quantities = [11,6]
# Output: 3
# Explanation: One optimal way is:
# - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
# - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
# The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

from math import ceil

class Solution:
    def no_distributions(self, quantities, s):
        # Function to calculate the total number of distributions with a given size (s)
        dis = 0
        for q in quantities:
            dis += ceil(q / s)
        return dis

    def minimizedMaximum(self, n: int, quantities):
        # Initialize low and high pointers for binary search based on quantities
        low, high = 1, max(quantities)
        # Initialize variable to store the result (minimized maximum distribution size)
        ans = 0

        # Binary search loop
        while low <= high:
            # Calculate mid value for distribution size
            mid = (low + high) // 2

            # Check the total number of distributions with mid distribution size
            dist = self.no_distributions(quantities, mid)

            # Adjust the pointers based on the comparison with n
            if dist <= n:
                # If total distributions with mid distribution size is less than or equal to n, search in the left half
                high = mid - 1
                ans = mid
            else:
                # If total distributions with mid distribution size is greater than n, search in the right half
                low = mid + 1

        # Return the minimized maximum distribution size required to achieve the given number of distributions (n)
        return ans


solution_object = Solution()
#Test case 1
result = solution_object.minimizedMaximum(7,[15,10,10])
print(result)
#Test case 2
result = solution_object.minimizedMaximum(6,[11,6])
print(result)