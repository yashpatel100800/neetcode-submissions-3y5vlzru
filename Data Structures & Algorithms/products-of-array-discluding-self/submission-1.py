class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefProd = [1]*(n+1)
        postProd = [1]*(n+1)

        mul = 1
        i = 1
        for num in nums:
            mul *= num
            print(i)
            prefProd[i] = mul
            i+=1

        i = n-1
        mul = 1
        for num in nums[::-1]:
            mul *= num
            postProd[i] = mul
            i-=1
        

        ans = []
        for i in range(len(nums)):
            ans.append(prefProd[i]*postProd[i+1])

        print(prefProd)
        print(postProd)
        print(ans)
        return ans
        