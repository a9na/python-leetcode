# 41. First Missing Positive
# Hard
#
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
#
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
# Constraints:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)  # Get the length of the input array
        
        # Step 1: Place each number in its correct position
        for i in range(n):
            # Continue swapping until nums[i] is in the correct position
            # or it is not in the valid range [1, n]
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1] to place it in the correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Find the first index where the number is incorrect
        for i in range(n):
            # If nums[i] is not equal to i + 1, return the missing number
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all numbers are in their correct positions, return n + 1
        return n + 1

# Test case:
param_1 = [3, 4, -1, 1]
ret = Solution().firstMissingPositive(param_1)
print(ret)  # Output: 2
