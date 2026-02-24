class Solution:
    def maxSubseq(self, s, k):
        stack = []
        
        for ch in s:
            while stack and k > 0 and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        # If removals still left
        if k > 0:
            stack = stack[:-k]
        
        return "".join(stack)
