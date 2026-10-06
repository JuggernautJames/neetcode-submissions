class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper = len(nums)
        curr = (int)(len(nums) / 2)
        lower = 0
        while True:
            if (nums[curr] == target):
                 return curr
            if (upper - lower<= 1):
                break
            if (nums[curr] > target):
                upper = curr
            else:
                lower = curr
            curr = (int)((upper - lower) / 2 + lower)
        return -1

