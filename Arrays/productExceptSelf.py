class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        curr = 1
        for i in range(n):
            answer[i] = curr
            curr *= nums[i]
        curr = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= curr
            curr *= nums[i]
        return answer
