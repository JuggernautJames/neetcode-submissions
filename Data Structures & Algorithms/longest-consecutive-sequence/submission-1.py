class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        longest = 1
        last = heapq.heappop(nums)
        thisCount = 1
        for _ in range(len(nums)):
            current = heapq.heappop(nums)
            if current == last:
                continue
            if last+1 == current:
                thisCount += 1
                longest = max(longest, thisCount)
            else:
                thisCount = 1
            last = current
            
        return longest