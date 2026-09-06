class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for i in s:
            if not i in hashS:
                hashS[i] = 0
            else:
                hashS[i] += 1
        
        for i in t:
            if not i in hashT:
                hashT[i] = 0
            else:
                hashT[i] += 1
        
        return hashS == hashT
        