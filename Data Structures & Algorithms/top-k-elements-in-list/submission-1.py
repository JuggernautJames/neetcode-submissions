class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i, val in enumerate(nums):
            if (val in count):
                count[val] -= 1
            else:
                count[val] = -1
        
        output = []
        heapNums = [(freq, num) for num, freq in count.items()]
        heapq.heapify(heapNums)
        for i in range(k):
            output.append(heapq.heappop(heapNums)[1])
        return output








































        """
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
        """