# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize low and high pointers for binary search
        low, high = 1, x
        # Initialize variable to store the result
        ans = 0

        # Binary search loop
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2

            # Check if mid*mid is equal to x
            if mid * mid == x:
                return mid
            # Check if mid*mid is less than x
            elif mid * mid < x:
                # Update ans to mid and search in the right half
                ans = mid
                low = mid + 1
            else:
                # If mid*mid is greater than x, search in the left half
                high = mid - 1
        
        # Return the result (ans represents the floor(sqrt(x)))
        return ans


solution_object = Solution()
#Test case 1
result = solution_object.mySqrt(4)
print(result)
#Test case 2
result = solution_object.mySqrt(8)
print(result)