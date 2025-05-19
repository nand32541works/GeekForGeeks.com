class Solution:
    def findPreSuc(self, root, key):
        self.arr = []
        self.solve(root)
        self.arr.sort()
        mn = float("inf")
        mnn = float("inf")
        ans1 = -1
        ans2 = -1
        for i in range(len(self.arr)):
            dif = key-self.arr[i]
            if dif>0:
                if dif<mn:
                    mn = dif
                    ans1 = self.arr[i]
            diff = self.arr[i]-key
            if diff>0:
                if diff<mnn:
                    mnn = diff
                    ans2 = self.arr[i]
        ans3 = Node(ans1)
        ans4 = Node(ans2)
        return [ans3,ans4]
        
    def solve(self,root):
        if not root:
            return
        self.arr.append(root.data)
        self.solve(root.left)
        self.solve(root.right)
