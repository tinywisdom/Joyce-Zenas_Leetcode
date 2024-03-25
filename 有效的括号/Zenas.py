class Solution:
    def isValid(self, s: str) -> bool:
        work_list = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                work_list.append(s[i])
            else:
                if len(work_list) == 0:
                    return False
                key = work_list.pop()
                if s[i] == ')' and key != '(':
                    return False
                elif s[i] == ']' and key != '[':
                    return False
                elif  s[i] == '}' and key != '{':
                    return False

        if len(work_list) != 0:
            return False
        
        return True
            