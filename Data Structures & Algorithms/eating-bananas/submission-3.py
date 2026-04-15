class Solution:


    def calculateHours(self, piles: List[int], bs: int) -> int:
        totalHours = 0 
        for i in piles:
            totalHours += math.ceil(i/bs)

        print(bs, totalHours)
        return totalHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        mid = 0
        ans = 0

        while(low<=high):
            mid = low + (high-low)//2
            hTook = self.calculateHours(piles,mid)
            if hTook > h:
                low = mid + 1
            elif hTook <= h:
                ans = mid
                high = mid - 1
        return ans
        
        