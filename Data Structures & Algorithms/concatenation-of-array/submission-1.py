class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        for i in range(length*2):
            j = i%length
            ans.append(nums[j])
        return ans