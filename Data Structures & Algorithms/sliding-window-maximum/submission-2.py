class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = r = 0
        output = []
        while(r<len(nums)):
            while q and q[-1]< nums[r]:
                q.pop()
            q.append(nums[r])

            

            if(r+1>=k):
                output.append(q[0])
                if(q[0]==nums[l]):
                    q.popleft()
                l+=1
            r+=1


        return output