# You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.
# Each train can only depart at an integer hour, so you may need to wait in between each train ride.
#For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.
# Input: dist = [1,3,2], hour = 6
# Output: 1
# Explanation: At speed 1:
# - The first train ride takes 1/1 = 1 hour.
# - Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
# - Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
# - You will arrive at exactly the 6 hour mark.


from math import ceil
class Solution:
    def findHours(self, dist, speed):
        # Function to calculate the total hours required to cover distances with a given speed
        h = 0
        n = len(dist) - 1

        # Calculate hours for each distance
        for i in range(n):
            h += ceil(dist[i] / speed)
        
        # Add hours for the last distance
        h += dist[n] / speed
        return h

    def minSpeedOnTime(self, dist, hour):
        # If the length of distances is greater than the ceiling of the given hour, it's impossible
        if len(dist) > ceil(hour):
            return -1

        # Initialize low and high pointers for binary search based on speeds
        low, high = 1, 10**7
        # Initialize variable to store the result (minimum speed)
        ans = -1

        # Binary search loop
        while low <= high:
            # Calculate mid value for speed
            mid = (low + high) // 2

            # Check if the total hours required with mid speed is less than or equal to the given hour
            no_hours = self.findHours(dist, mid)
            if no_hours <= hour:
                # If possible, update ans to mid and search in the left half
                high = mid - 1
                ans = mid
            else:
                # If not possible, search in the right half
                low = mid + 1

        # Return the minimum speed required to cover distances within the given hour
        return ans


solution_object = Solution()
#Test case 1
result = solution_object.minSpeedOnTime([1,3,2],6)
print(result)
#Test case 2
result = solution_object.minSpeedOnTime([1,3,2],2.7)
print(result)