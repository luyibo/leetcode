__author__ = 'lyb-mac'
def plusOne(digits):
        '''temp = ''.join(str(i) for i in digits)
        if len(temp)==1:
            if temp=='9':
                return [1,0]
            else: return [int(temp)+1]
        else:
            if (temp[0]=='0'):
                if temp[1]=='9':
                    temp1 = int(temp)+1
                    if len(str(temp1))==len(temp):
                        temp2 =[0]+[int(i) for i in str(temp1)]
                    else:
                        temp2=[0]+[int(i) for i in str(temp1)]
                else: temp2=[0]+[int(i) for i in str(int(temp)+1)]
            else:
                temp2=[int(i) for i in str(int(temp)+1)]
        return temp2'''
        digits[-1] += 1
        i = len(digits)-1
        while digits[i]==10:
            digits[i] = 0
            if i>0:
                digits[i-1] += 1
                i -= 1
            else:
                digits.insert(0,1)
        return digits

print plusOne([0,9,9,9])