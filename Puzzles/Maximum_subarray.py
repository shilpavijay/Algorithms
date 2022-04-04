'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_sum = current_sum = nums[0]
        for each in nums[1:]:
            current_sum = max(each, current_sum+each) #works for neg edge conditions
            best_sum = max(best_sum,current_sum)
        return best_sum
        