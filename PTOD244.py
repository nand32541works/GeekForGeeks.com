class Solution:
    def nextGreater(self, arr):
        n = len(arr)
        idx = 0
        for i in range(n):
            if arr[i] > arr[idx]:
                idx = i
        sol = [-1] * n
        st = []
        for i in range(idx + 1, idx + n + 1):
            while st and arr[i % n] > arr[st[-1]]:
                sol[st[-1]] = arr[i % n]
                st.pop()
            st.append(i % n)
        return sol
