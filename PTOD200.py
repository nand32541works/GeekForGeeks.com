class Solution:
	def isPalinSent(self, s):
		m=[]
        for i in s:
            if i.isalnum() and i!=" ":
                p=i.lower()
                m.append(p)
                
        n="".join(m)       
        return (n==n[::-1])
