class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)
        highest = 0
        for num in nums:
            if not num-1 in numsSet:
                i = num
                count = 1
                while i+1 in numsSet:
                    count += 1
                    i += 1
                highest = max(highest, count)
        return highest
        