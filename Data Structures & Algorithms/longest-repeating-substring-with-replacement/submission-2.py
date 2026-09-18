class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        maxchar = 0
        freq = {}
        for right, value in enumerate(s):
            freq[value] = freq.get(value, 0) + 1
            maxchar = max(maxchar, freq[value])
            if right - left + 1 - maxchar > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
