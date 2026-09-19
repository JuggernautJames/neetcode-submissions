from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        windowItems = {char: -freq for char, freq in Counter(s1).items()}
        requiredmatches = len(s1)
        for right in range(0, len(s2)):
            newchar = s2[right]
            charcount = windowItems.get(newchar, 0)
            if charcount < 0:
                requiredmatches -= 1
            windowItems[newchar] = charcount + 1
            if right - left > len(s1)-1 and s2[left] in windowItems:
                windowItems[s2[left]] -= 1
                if windowItems[s2[left]] < 0:
                    requiredmatches += 1
                left += 1
            print(requiredmatches)
            print(windowItems)
            if requiredmatches == 0:
                return True
        return False

