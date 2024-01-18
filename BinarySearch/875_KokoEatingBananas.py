# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.


import math

class Solution:
    def no_of_hours(self, k, piles):
        # Calculate total hours required to eat all piles with the given eating speed (k)
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours

    def minEatingSpeed(self, piles, h) -> int:
        # Initialize low and high pointers for binary search
        low, high = 1, max(piles)
        # Initialize variable to store the minimum eating speed
        k = 0

        # Binary search loop
        while low <= high:
            # Calculate mid eating speed
            mid = (low + high) // 2

            # Check if total hours required with mid eating speed is less than or equal to h
            if self.no_of_hours(mid, piles) <= h:
                # Update k to mid and search in the left half
                k = mid
                high = mid - 1
            else:
                # If total hours is greater than h, search in the right half
                low = mid + 1

        # Return the minimum eating speed
        return k


solution_object = Solution()
#Test case 1
result = solution_object.minEatingSpeed([3,6,7,11],8)
print(result)
#Test case 2
result = solution_object.minEatingSpeed([30,11,23,4,20],5)
print(result)