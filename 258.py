__author__ = 'lyb-mac'
def addDigits(num):
        """
        :type num: int
        :rtype: int
        """
        #my solution
        '''length = len(str(num))
        while length>1:
            a = [int(i) for i in str(num)]
            print a
            sum1 = 0
            for i in a:
                sum1 = sum1+i
            length = len(str(sum1))
            num = sum1
        print num'''
        #excellent solution
        if num==0:return 0
        elif num % 9 ==0:return 9
        else:return num%9
print addDigits(178)