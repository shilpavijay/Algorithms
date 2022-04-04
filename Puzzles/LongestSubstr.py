# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        longest = ""
        substr = ""
        for letter in s:
            findidx = substr.find(letter)
            if findidx == -1:
                substr = substr + letter
            else: 
                if len(substr) > len(longest):
                    longest = substr
                substr = substr + letter
                substr = substr[findidx+1:]
                  
        if len(substr) > len(longest):
            longest = substr
        return len(longest)

        
                
                
                
        