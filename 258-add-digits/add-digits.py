class Solution(object):
    def addDigits(self, num):
        s = 0
        temp = num

        while temp > 9:
            s = 0

            while temp > 0:
                digit = temp % 10
                s = digit + s
                temp = temp // 10

            temp = s

        return temp