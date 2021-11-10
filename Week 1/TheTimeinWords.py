
import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
single = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
double = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
temp = ['twenty', 'thirty', 'forty', 'fifty' ]
def numToString(num):    
    if num<10 :      
        return single[num]  
    if num<20 :
        return double[num-10]
    return temp[int(num/10)-2]+' '+single[num%10]
        
def timeInWords(h, m):
    if m>30 :
        hour = numToString(h+1)
        if m==45 :
            return 'quarter to '+hour
        return numToString(60-m)+' minutes to '+hour
    hour = numToString(h)
    if m==0:
        return hour+' o\' clock'
    if m<=30 :
        if m==30:
            min= 'half'
        elif m==15:
            min= 'quarter'
        elif m==1:
            min= 'one minute'
        else :
            min = numToString(m)+' minutes'
        return min+' past '+hour


if __name__ == '__main__':    

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)
    print(result)

