class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            largest = float('-inf')
            for j in range(i+1, len(arr)):
                largest = max(largest, arr[j])
            arr[i] = largest
        arr[-1] = -1
        return arr
