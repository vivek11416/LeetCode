class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        for p in s:
            if p in ['(', '[', '{']:
                mystack.append(p)
            elif p == ')':
                try:
                    assert mystack.pop() == '('
                except:
                    return False
            elif p == ']':
                try:
                    assert mystack.pop() == '['
                except:
                    return False
            elif p == '}':
                try:
                    assert mystack.pop() == '{'
                except:
                    return False
        return True if not mystack else False
        