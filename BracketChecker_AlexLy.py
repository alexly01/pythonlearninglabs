'''
name: Alexander Ly
studentID: 027744520

assignment:PA1
'''

import sys

class Solution:
    def pa1(self, s: str) -> bool:
        open_brackets = "{[("
        closed_brackets = "}])"
        
        # Create dictionary
        all_brackets = {')': '(', '}': '{', ']': '['}
        
        # Keep track of brackets which are open
        stack = []

        for char in s:
            if char in open_brackets:
                # Push onto stack
                stack.append(char)

            elif char in closed_brackets:
                if len(stack) == 0:
                    return False

                if stack[-1] == all_brackets[char]:
                    # Pop out of stack
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

if __name__ == '__main__':
    if len(sys.argv) > 1:
        s = sys.argv[1]
    else:
        s = input("Please enter a string: ")
    
    obj = Solution()
    ret = obj.pa1(s)
    print(ret)