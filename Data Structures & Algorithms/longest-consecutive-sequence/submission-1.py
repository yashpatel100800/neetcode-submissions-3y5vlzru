class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 1
        count = 1
        nums.sort()
        if len(nums)<=1:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
                ans = max(ans, count)
            elif nums[i]==nums[i-1]:
                continue
            else:
                count = 1
        return ans
        