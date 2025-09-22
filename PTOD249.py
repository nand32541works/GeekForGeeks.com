class Solution:
    def reverseQueue(self, q):
        st = []
        while q:
            st.append(q[0])
            q.popleft()
        while st:
            q.append(st.pop())
