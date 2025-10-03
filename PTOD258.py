class Solution:
    def buildExpr(self, res, expr, digits, target, idx, evalVal, last):
        if idx == len(digits):
            if evalVal == target:
                res.append(expr)
            return
        for i in range(idx, len(digits)):
            if i != idx and digits[idx] == '0':
                break
            part = digits[idx:i + 1]
            num = int(part)
            if idx == 0:
                self.buildExpr(res, part, digits, target, i + 1, num, num)
            else:
                self.buildExpr(res, expr + "+" + part, digits, target, i + 1,
                               evalVal + num, num)
                self.buildExpr(res, expr + "-" + part, digits, target, i + 1,
                               evalVal - num, -num)
                self.buildExpr(res, expr + "*" + part, digits, target, i + 1,
                               evalVal - last + last * num, last * num)
    def findExpr(self, s, target):
        res = []
        self.buildExpr(res, "", s, target, 0, 0, 0)
        return res
