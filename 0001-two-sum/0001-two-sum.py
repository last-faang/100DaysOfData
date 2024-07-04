class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            index_map[num] = i

        for i, num in enumerate(nums):
            gap = target - num
            
            if gap in index_map and index_map[gap] != i:
                return [i, index_map[gap]]
