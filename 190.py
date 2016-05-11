__author__ = 'lyb-mac'
def reverseBits(self, n):
    return int(bin(n)[2:][::-1]+'0'*(32-len(bin(n)[2:][::-1])),2)