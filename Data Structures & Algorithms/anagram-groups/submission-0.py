class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
