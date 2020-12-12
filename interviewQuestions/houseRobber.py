# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security system connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of
# money of each house, determine the maximum amount of money you can
# rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
class Solution:
    def rob(self, nums: list) -> int:  # O(n)
        # Fill this in
        option1 = 0
        option2 = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                option1 += nums[i]
            else:
                option2 += nums[i]
        return option1 if option1 > option2 else option2

    def rob2(self, nums: list) -> int:  # O(2n) --> O(n)
        option1 = 0
        option2 = 0
        for i in range(0, len(nums), 2):
            option1 += nums[i]
        for i in range(1, len(nums), 2):
            option2 += nums[i]
        return option1 if option1 > option2 else option2

solution = Solution()
# nums = [1,2,3,1]
nums = [2, 7, 9, 3, 1]
print(solution.rob(nums))
print(solution.rob2(nums))
