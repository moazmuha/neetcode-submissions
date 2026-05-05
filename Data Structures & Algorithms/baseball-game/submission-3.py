class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lastAdded = []
        score = 0
        for x in operations:
            if x == '+':
                toAdd = lastAdded[-1] + lastAdded[-2]
            elif x == 'D':
                toAdd = lastAdded[-1]*2
            elif x == 'C':
                toAdd = lastAdded.pop()*-1
            else:
                toAdd = int(x)
            if x != 'C': lastAdded.append(toAdd)
            score += toAdd
        return score
            
