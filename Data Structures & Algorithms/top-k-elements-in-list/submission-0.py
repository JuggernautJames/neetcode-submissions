class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFreq = {}
        for i in nums:
            if not i in numsFreq:
                numsFreq[i] = 0
            numsFreq[i] += 1
        sortedFreq = list(sorted(numsFreq.items(), key=lambda item: item[1], reverse = True))
        ans = []
        for i in range(k):
            ans.append(sortedFreq[i][0])
        return ans