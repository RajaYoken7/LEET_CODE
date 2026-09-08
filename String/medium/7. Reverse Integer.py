class Solution(object):
    def reverse(self, x):
        target=0
        sign=1
        if x<0:
            sign=-1
            x=-x
        while x>0:
            ld = x%10
            target = (target*10) +ld 
            x = x//10
        if target<-2**31 or target>2**31-1:
            return 0
        else:
            return target*sign
