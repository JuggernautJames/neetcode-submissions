class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0;
        end = len(heights) - 1
        ans = 0
        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            ans = max(area, ans)
            if (heights[start] < heights[end]):
                start+=1
            else:
                end-=1
        return ans
