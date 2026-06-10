class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        c=0
        temp=num
        while temp>0 :
            digit=temp%10
            if num%digit==0:
                c=c+1
            temp=temp//10
        return c
        