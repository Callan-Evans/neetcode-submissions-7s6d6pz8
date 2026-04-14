class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array = []
        for i in range (1,3):
            for num in nums:
                new_array.append(num)
        return new_array