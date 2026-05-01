class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lastValIndex = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[lastValIndex] = nums[i]
                lastValIndex += 1
        return lastValIndex
