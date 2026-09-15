class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            count = [0] * 26
            for char in i:
                count[ord(char)-97] += 1
            countTuple = tuple(count)
            if countTuple in ans:
                ans[countTuple].append(i)
            else:
                ans[countTuple] = [i]
        return list(ans.values())
        
        
        
        


























        
        
        
        
        """
        ans = {}
        for word in strs:
            alphabet=[0]*26
            for char in word:
                alphabet[ord(char) - ord('a')] += 1
            key = tuple(alphabet)
            if not key in ans:
                ans[key] = []
            ans[key].append(word)
        return list(ans.values())
        """
