class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, current, right = 0, 0, len(nums) - 1

        while current < right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
            if nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
            if nums[right] == 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            if nums[left] == 2:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1

            current += 1
