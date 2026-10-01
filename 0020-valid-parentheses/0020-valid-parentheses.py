class Solution(object):
    def isValid(self, s):
        st = []
        for i in s:
            if len(st)==0:
                st.append(i)
            else:
                if i == ')':
                    if st[-1]=='(':
                        st.pop()
                    else:
                        st.append(i)
                elif i == ']':
                    if st[-1]=='[':
                        st.pop()
                    else:
                        st.append(i)
                elif i == '}':
                    if st[-1]=='{':
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
        return len(st)==0
                