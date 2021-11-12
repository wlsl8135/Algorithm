#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # n은 체스판 크기
    # k는 방해물 갯수
    # r_q, c_q는 퀸 위치
    # n이 홀 수일때 대각선 최대 2*(n-1) 개, 최소 (n-1)개 
    # n이 짝 수일때 대각선 최대 2*(n-2)+1개 최소 (n-1)개 
    # Write your code here    
    
    max_answer=2*(n-1)
    upper_right = max(0, min(n-c_q, n-r_q))
    upper_left = max(0,min(c_q-1, n-r_q))
    down_right  = max(0, min(n-c_q, r_q-1))
    dwon_left = max(min(c_q-1, r_q-1), 0)
    max_answer= max_answer+upper_right+upper_left+down_right+dwon_left
    
    max_list= [0]*8
    for obstacle in obstacles:
        #obstacle=>[행, 열]
        #check_horizontal  열검사  
        if obstacle[0] == r_q : 
            if c_q <obstacle[1]: # 장애물이 오른쪽에 있을 때,
                max_list[2]=max(max_list[2], n-obstacle[1]+1)
            else : 
                max_list[6]=max(max_list[6], obstacle[1])
        #check_vertical
        if obstacle[1] == c_q :
            if r_q <obstacle[0]: # 장애물이 위쪽에 있을 때
                max_list[0]=max(max_list[0], n-obstacle[0]+1)
            else : 
                max_list[4]=max(max_list[4], obstacle[0])
        #check y=x diag
        if r_q-c_q == obstacle[0]-obstacle[1] :
            if r_q <obstacle[0] and c_q < obstacle[1]: #장애물이 우측 상단에 있을 때
                max_list[1]=max(max_list[1], min(n-obstacle[1]+1, n-obstacle[0]+1))
            else : #장애물이 좌측 하단에 있을때
                max_list[5]=max(max_list[5], min(obstacle[1], obstacle[0]))
        #check_diag y=-x
        if r_q+c_q == obstacle[0]+obstacle[1] :
            if r_q > obstacle[0] and c_q < obstacle[1]:
                max_list[3]=max(max_list[3], min(obstacle[0], n-obstacle[1]+1))
            else : 
                max_list[7]=max(max_list[7], min(obstacle[1], n-obstacle[0]+1))
    sum=0
    for temp in max_list:
        sum+=temp
    return max_answer-sum




if __name__ == '__main__':    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)