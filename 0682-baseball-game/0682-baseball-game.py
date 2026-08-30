class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for op in operations:
            if op.isdigit() or (op[0] == '-' and op[1:].isdigit()):
                st.append(int(op))

            elif op == 'C':
                st.pop()

            elif op == 'D':
                st.append(st[-1] * 2)

            elif op == '+':
                st.append(st[-1] + st[-2])

        return sum(st)