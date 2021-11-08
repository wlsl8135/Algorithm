#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
# 더했을 때 나머지가 0인 경우는 두 수 모두 k의 배수인 경우 (n%k==0), t를 n%k의 값이라고 했을 때, 두 수가 t, k-t 인 경우이다.
# 그걸 dict로 만들어서 문제 해결
    
def nonDivisibleSubset(k, s):
    divisibelDict = {       
    }
    len = 0 
    for num in s:        
        if num%k in divisibelDict.keys():
            divisibelDict[num%k].append(num)
        else : 
            divisibelDict[num%k] = []       
            divisibelDict[num%k].append(num)       
    check = [0, k/2]       
    for key in divisibelDict.keys():
        temp=0
        if key in check :
            continue
        else : 
            if k-key in divisibelDict.keys():
                temp = max(list(set(divisibelDict[key])).__len__(), list(set(divisibelDict[k-key])).__len__())
                check.append(k-key)
            else :
                temp = len(divisibelDict[key])
            len+=temp
    if 0 in divisibelDict.keys():
        len+=1
    if k/2 in divisibelDict.keys():
        len+=1
    return len
        


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print(result)