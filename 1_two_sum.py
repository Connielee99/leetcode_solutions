class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in num_idx:
                return [num_idx[diff], i]
            else:
                num_idx[num] = i
        return []