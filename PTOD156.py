class Solution:
    def minSum(self, arr):
        arr.sort()
        n1, n2 = [], []
        parity = 0
        for i in arr:
            if parity == 0:
                n1.append(i)
            else:
                n2.append(i)
            parity ^= 1
        n1 = n1[::-1]
        n2 = n2[::-1]
        n1_ptr, n2_ptr = 0, 0
        carry = 0
        res = []
        while n1_ptr < len(n1) and n2_ptr < len(n2):
            val = n1[n1_ptr] + n2[n2_ptr] + carry
            res.append(str(val % 10))
            carry = val // 10
            n1_ptr += 1
            n2_ptr += 1
        while n1_ptr < len(n1):
            val = n1[n1_ptr] + carry
            res.append(str(val % 10))
            carry = val // 10
            n1_ptr += 1
        while n2_ptr < len(n2):
            val = n2[n2_ptr] + carry
            res.append(str(val % 10))
            carry = val // 10
            n2_ptr += 1
        if carry:
            res.append('1')
        return "".join(res)[::-1].lstrip('0')
