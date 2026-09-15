class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = "".join(char.lower() for char in s if char.isalnum())
        length = len(alphaNum)
        for i in range(math.floor(length / 2)):
            left = alphaNum[i]
            right = alphaNum[length - i - 1]
            if (not left == right):
                return False
        return True