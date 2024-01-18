# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

class Solution:
    def minDays(self, bloomDay, m, k):
        # If the total flowers needed (m * k) is greater than the total flowers available, it's impossible
        if m * k > len(bloomDay):
            return -1

        # Function to check if it's possible to make bouquets with a given number of days
        def can_make_bouquets(days):
            consecutive_bouquets, count = 0, 0

            for bloom in bloomDay:
                # Check if the bloom is within the allowed days
                if bloom <= days:
                    count += 1
                    # If enough flowers for a bouquet are collected, increment the bouquet count
                    if count == k:
                        consecutive_bouquets += 1
                        count = 0
                else:
                    # Reset count if the bloom is not within the allowed days
                    count = 0

            return consecutive_bouquets >= m

        # Initialize low and high pointers for binary search based on bloomDay values
        low, high = min(bloomDay), max(bloomDay)
        # Initialize variable to store the result (minimum days)
        ans = -1

        # Binary search loop
        while low <= high:
            # Calculate mid value for days
            mid = (low + high) // 2

            # Check if it's possible to make bouquets with mid days
            if can_make_bouquets(mid):
                # If possible, update ans to mid and search in the left half
                ans = mid
                high = mid - 1
            else:
                # If not possible, search in the right half
                low = mid + 1

        # Return the minimum days required to make m bouquets with k flowers each
        return ans


solution_object = Solution()
#Test case 1
result = solution_object.minDays([1,10,3,10,2],3,1)
print(result)
#Test case 2
result = solution_object.minDays([7,7,7,7,12,7,7],2,3)
print(result)