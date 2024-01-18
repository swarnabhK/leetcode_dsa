# You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.
# Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.
# You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
# Input: time = [1,2,3], totalTrips = 5
# Output: 3
# Explanation:
# - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
#   The total number of trips completed is 1 + 0 + 0 = 1.
# - At time t = 2, the number of trips completed by each bus are [2,1,0]. 
#   The total number of trips completed is 2 + 1 + 0 = 3.
# - At time t = 3, the number of trips completed by each bus are [3,1,1]. 
#   The total number of trips completed is 3 + 1 + 1 = 5.
# So the minimum time needed for all buses to complete at least 5 trips is 3.




class Solution:
    def noTrips(self, time, k):
        # Function to calculate the total number of trips with given time and capacity (k)
        t = 0
        for tm in time:
            t += k // tm
        return t

    def minimumTime(self, time, totalTrips: int) -> int:
        # Initialize left and right pointers for binary search based on time and totalTrips
        left, right = 1, totalTrips * min(time)
        # Initialize variable to store the result (minimum time)
        ans = 1

        # Binary search loop
        while left <= right:
            # Calculate mid value for time
            mid = (left + right) // 2

            # Check the total number of trips with mid time
            n_trips = self.noTrips(time, mid)

            # Adjust the pointers based on the comparison with totalTrips
            if n_trips < totalTrips:
                # If total trips with mid time is less than required, search in the right half
                left = mid + 1
            else:
                # If total trips with mid time is greater or equal, update ans and search in the left half
                ans = mid
                right = mid - 1

        # Return the minimum time required to achieve the given totalTrips
        return ans




solution_object = Solution()
#Test case 1
result = solution_object.minimumTime([1,2,3],5)
print(result)
#Test case 2
result = solution_object.minimumTime([2],1)
print(result)