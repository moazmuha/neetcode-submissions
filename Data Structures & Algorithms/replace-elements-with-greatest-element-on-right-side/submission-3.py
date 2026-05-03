class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSoFar = -1
        for i in range(len(arr)-1, -1, -1):
            num = arr[i]
            arr[i] = maxSoFar
            maxSoFar = max(num, maxSoFar)
        return arr 