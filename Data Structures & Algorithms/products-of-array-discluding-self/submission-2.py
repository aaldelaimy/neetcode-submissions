class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)
        prefix = [1] * len(nums)
        pre = 1
        postfix = [1] * len(nums)
        post = 1

        for i in range(len(nums)):
            prefix[i] = pre
            pre *= nums[i]
        for i in range(len(nums) -1 , -1, -1):
            postfix[i] = post
            post *= nums[i]
        for i in range(len(nums)):
            output[i] = (postfix[i] * prefix[i])
        return output





