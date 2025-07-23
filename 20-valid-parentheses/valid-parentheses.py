class Solution:
    def isValid(self, s: str) -> bool:
        st=deque()
        for ch in s:
            if ch in '({[':
                st.append(ch)
            elif ch==')' and st and st[-1]=='(':
                st.pop()
            elif ch=='}' and st and st[-1]=='{':
                st.pop()
            elif ch==']' and st and st[-1]=='[':
                st.pop()
            else:
                return False
        return len(st)==0