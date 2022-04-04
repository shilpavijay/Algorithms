'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #SOLUTION 1:
        intersection = []
        setinter = set(nums1).intersection(set(nums2))
        for each in setinter:
            if nums1.count(each) == nums2.count(each) or nums1.count(each) < nums2.count(each):
                intersection.extend([each for x in range(0,nums1.count(each))])
            else:
                intersection.extend([each for x in range(0,nums2.count(each))])
        return intersection
                
        #SOLUTION 2:        
        # intersection = []
        # if len(nums1) > len(nums2):
        #     iterlist = nums2
        #     comparelist = nums1
        # else:
        #     iterlist = nums1
        #     comparelist = nums2
        # for each in iterlist:
        #     try:
        #         idx = comparelist.index(each)
        #         intersection.append(comparelist[idx])
        #         comparelist.pop(idx)
        #     except:
        #         continue
        # return intersection