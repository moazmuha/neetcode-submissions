class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"{", "(", "["}
        l = []
        for c in s:
            if c in opening:
                l.append(c)
            if l:
                if c == "}" and l.pop() != "{":
                    return False
                elif c == ")" and l.pop() != "(":
                    return False
                elif c == "]" and l.pop() != "[":
                    return False
            else:
                return False
        if not l:
            return True
        return False