class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 999999
        sell = 0
        leftArr = prices;
        rightArr = []
        for i in range(len(prices)-1):
            price = leftArr.pop()
            rightArr.append(price)
            currBuy = min(leftArr)
            currSell = max(rightArr)
            if currSell - currBuy > sell - buy:
                buy = currBuy
                sell = currSell
        return 0 if (sell - buy < 0) else sell - buy