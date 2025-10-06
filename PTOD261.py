class Solution:
    def bottomView(self, root):
        def findLeftExtreme(root):
                if not root:
                    return 0
                return min(findLeftExtreme(root.left)-1, findLeftExtreme(root.right)+1)
        def findRightExtreme(root):
                if not root:
                    return 0
                return max(-1+findRightExtreme(root.left), 1+findRightExtreme(root.right))
        l=findLeftExtreme(root)+1
        r=findRightExtreme(root)-1
        dic={}
        for i in range(r-l+1):
            dic[i]=0
        arr=[0]*(r-l+1)
        l=abs(l)
        def helper(root, val,lvl):
            if not root:
                return
            if not dic[l+val] or dic[l+val]<lvl:
                arr[l+val]=root.data
                dic[l+val]=lvl
            helper(root.right,val+1,lvl+1)
            helper(root.left, val-1,lvl+1)
            
        helper(root, 0,0)
        return arr
