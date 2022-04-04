# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Time Complexity - O(n)
        d={}
        try:
            for idx,each in enumerate(nums):
                complement = target - each
                if d.__contains__(complement):
                    return (d[complement],idx)
                d.update({each:idx})
        except:
            print("No two sums found")
        
    # Alternate Solution - O(n)+O(n) or O(2n)
    def twoSum2(self, nums, target):
        sub={each:target-each for each in nums}
        for (key,value) in sub.items():
            try:
                if key+value == target:
                    key_index=nums.index(key)
                    nums[key_index] = -999
                    return(key_index,nums.index(value))
            except:
                continue
        