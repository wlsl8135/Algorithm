real_board = [] 
def search(x, y, num, length, chk_board):    
    global real_board    
    max_length = -1
    chk_board[y][x]=1
    if x+1<4 and real_board[y][x] == real_board[y][x+1] :
        if chk_board[y][x+1] ==0:
            max_length= max(max_length, search(x+1, y, num, length+1, chk_board))
    if y+1<4 and real_board[y][x] == real_board[y+1][x] : 
        if chk_board[y+1][x] ==0:
            max_length= max(max_length, search(x, y+1, num, length+1, chk_board))
    if x-1>=0 and real_board[y][x] == real_board[y][x-1] : 
        if chk_board[y][x-1] ==0:
            max_length = max(max_length, search(x-1, y, num, length+1, chk_board))
    if y-1>=0 and real_board[y][x] == real_board[y-1][x] : 
        if chk_board[y-1][x] ==0:
            max_length = max(max_length, search(x, y-1, num, length+1, chk_board))
    return max(length, max_length)

def solution(board):    
    global real_board       
    answer = -1
    for y in range(4):
        for x in range(4):
            chk_board = [] 
            for _ in range(4):                        
                chk_board.append([0,0,0,0])
            answer=max(answer, 
                    search(x, y, real_board[y][x], 0, chk_board)
            )
    if answer==0 or answer==-1:
        return -1
    else : 
        return answer+1

real_board=[]
for i in range(4):
    real_board.append(list(map(int, input().split())))
print(solution(real_board))