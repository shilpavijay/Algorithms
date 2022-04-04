'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

from collections import deque
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
             
        if digits == "":
          return []      
    
        phone_keys = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        
        q = deque(phone_keys[int(digits[0])])
        
        for i in range(1,len(digits)):
            s = len(q)
            while s:
                out = q.popleft()
                for j in phone_keys[int(digits[i])]:
                    q.append(out+j)
                s -=1
        return q    

s = Solution()
digits = "23"
print(s.letterCombinations(digits))             
