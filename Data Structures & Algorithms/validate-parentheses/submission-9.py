class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        l = []
        for c in s:
            if c in closeToOpen:
                if l:
                    last = l.pop()
                    if last != closeToOpen[c]:
                        return False
                else:
                    return False
            else:
                l.append(c)
        return not l

                    
