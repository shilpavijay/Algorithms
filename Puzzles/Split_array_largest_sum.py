'''
Given an array nums which consists of non-negative integers and an integer m, you can split the array 
into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
'''
import sys
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        nlen = len(nums)
        dp = [[sys.maxsize] * (m + 1) for _ in range(nlen + 1)]
        # print(dp)
        dp[0][0] = 0
        presum = [0] * (nlen + 1)
        # print(presum)
        for i, n in enumerate(nums):
            presum[i + 1] = n + presum[i]
        
        # print(presum)
        # print(dp)
        for i in range(1, nlen + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], presum[i] - presum[k]))
        #             print("printing dp[k][j-1] and presum[i] and [k] -> dp[i][j]")
        #             print(dp[k][j - 1])
        #             print(presum[i])
        #             print(presum[k])
        #             print(dp[i][j])
        # print(dp)
        return dp[nlen][m]

s= Solution()
print(s.splitArray([7,2,5,10,8],2))        