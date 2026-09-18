class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1: return 0
        if len(s) == 1: return 1
        charmap = {}
        maxlength = 0
        left = 0
        for right, char in enumerate(s):
            if char in charmap and charmap[char] >= left:
                left = charmap[char] + 1
            charmap[char] = right
            maxlength = max(maxlength, right - left + 1)
        return maxlength