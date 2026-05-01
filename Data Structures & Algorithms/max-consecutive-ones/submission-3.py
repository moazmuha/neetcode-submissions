class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1s = 0
        if len(nums) >= 1:
            consec1s = 0
            for num in nums:
                if num == 1:
                    consec1s += 1
                else: 
                    max1s = max(consec1s, max1s)
                    consec1s = 0 
            max1s = max(consec1s, max1s)
        return max1s