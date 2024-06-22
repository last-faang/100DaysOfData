class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left <= right:
            new_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, new_area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
        