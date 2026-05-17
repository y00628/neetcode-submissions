from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = deque([])
        exp = {"+", "-", "*", "/"}

        for tk in tokens:
            print(st)
            if tk not in exp:
                st.append(tk)
                continue

            right, left = int(st.pop()), int(st.pop())

            print(f'{left} {tk} {right}')

            if tk == "+":
                st.append(str(left+right))
            elif tk == "-":
                st.append(str(left-right))
            elif tk == "*":
                st.append(str(left*right))
            elif left%right != 0 and left/right < 0:
                st.append(str(left//right+1))
            else:
                st.append(str(left//right))

        return int(st.pop())
            
                
