# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.



class Solution:
    def shipPossible(self, k, weights, days):
        # Function to check if it's possible to ship all weights within given days using a specific capacity (k)
        s, no_days = 0, 1

        for weight in weights:
            s += weight
            # If the cumulative weight exceeds the capacity, reset s to the current weight and increment days count
            if s > k:
                s = weight
                no_days += 1

        # Check if the number of days required is less than or equal to the given days
        return no_days <= days

    def shipWithinDays(self, weights, days):
        # Initialize low and high pointers for binary search based on weights
        low, high = max(weights), sum(weights)
        # Initialize variable to store the result (minimum capacity)
        ans = 0

        # Binary search loop
        while low <= high:
            # Calculate mid value for capacity
            mid = (low + high) // 2

            # Check if it's possible to ship all weights within given days using mid capacity
            if self.shipPossible(mid, weights, days):
                # If possible, update ans to mid and search in the left half
                ans = mid
                high = mid - 1
            else:
                # If not possible, search in the right half
                low = mid + 1

        # Return the minimum capacity required to ship all weights within given days
        return ans



solution_object = Solution()
#Test case 1
result = solution_object.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5)
print(result)
#Test case 2
result = solution_object.shipWithinDays([3,2,2,4,1,4],3)
print(result)