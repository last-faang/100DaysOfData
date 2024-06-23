class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0

        while (left <= right and right < len(nums)):
            if (nums[right] != 0):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            
            right += 1
        