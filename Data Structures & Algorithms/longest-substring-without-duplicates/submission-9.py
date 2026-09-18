class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1: return 0
        if len(s) == 1: return 1
        frequency = set([s[0]])
        substring = [s[0]]
        maxLength = 0
        left = 0
        right = 0
        while right < len(s) - 1:
            right += 1
            newchar = s[right]
            if newchar in frequency:
                poppedChar = None
                while poppedChar != newchar:
                    poppedChar = substring[left]
                    frequency.remove(poppedChar)
                    left += 1
            substring.append(newchar)
            frequency.add(newchar)
            maxLength = max(right - left + 1, maxLength)
        return maxLength