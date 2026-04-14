class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        top_number = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter +=1
                if counter > top_number:
                    top_number = counter
            else:
                counter = 0
        return top_number
        