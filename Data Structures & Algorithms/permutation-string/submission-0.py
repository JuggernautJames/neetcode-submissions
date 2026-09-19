from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        windowItems = {char: -freq for char, freq in Counter(s1).items()}
        for right in range(0, len(s2)):
            newchar = s2[right]
            windowItems[newchar] = windowItems.get(newchar, 0) + 1
            if right - left > len(s1)-1 and s2[left] in windowItems:
                windowItems[s2[left]] -= 1
                left += 1

            print(windowItems)
            if all(value == 0 for value in windowItems.values()):
                return True
        return False

