class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        parentheses_dict = {")": "(", "}": "{", "]": "["}
        stack = []

        for letter in s:
            if letter not in parentheses_dict:
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                
                popped = stack.pop()
                if popped != parentheses_dict[letter]:
                    return False
                
        return len(stack) == 0
