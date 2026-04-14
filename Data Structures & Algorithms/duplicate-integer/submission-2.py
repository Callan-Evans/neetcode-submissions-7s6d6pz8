class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        for number in num_set:
            if nums.count(number) >= 2:
                return True
        return False