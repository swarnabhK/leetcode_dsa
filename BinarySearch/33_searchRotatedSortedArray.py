# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

class Solution:
    def search(self, nums, target):
        # Initialize low and high pointers for binary search
        low, high = 0, len(nums) - 1
        
        # Binary search loop
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2
            
            # Check if target is found at mid
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                # Check if target is within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    # If not, search in the right half
                    low = mid + 1
            # Check if right half is sorted
            elif nums[mid] <= nums[high]:
                # Check if target is within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    # If not, search in the left half
                    high = mid - 1
        
        # If target is not found, return -1
        return -1


solution_object = Solution()
#Test case 1
result = solution_object.search([4,5,6,7,0,1,2],0)
print(result)
#Test case 2
result = solution_object.search([4,5,6,7,0,1,2],3)
print(result)