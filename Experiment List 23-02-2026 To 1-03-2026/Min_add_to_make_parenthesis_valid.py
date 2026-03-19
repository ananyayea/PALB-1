class Solution:
    def minParentheses(self, s: str) -> int:
        balance = 0
        open_needed = 0
        
        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ')'
                if balance > 0:
                    balance -= 1
                else:
                    open_needed += 1
        
        return open_needed + balance
