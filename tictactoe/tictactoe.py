"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx = 0
    counto = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == X :
                countx += 1
            if  board[row][col] == O :
                counto += 1   
    return X if countx == counto else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possible_moves.add((row,col))
    return possible_moves            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x,y) = action
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        raise IndexError
    ActionArray = [row[:] for row in board]
    ActionArray[x][y] = player(board)
    return ActionArray 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_Rows(board,X) or check_columns(board,X) or check_TopBottomDiagonal(board,X) or check_BottomTopDiagonal(board,X):
        return X
    elif check_Rows(board,O) or check_columns(board,O) or check_TopBottomDiagonal(board,O) or check_BottomTopDiagonal(board,O):
        return O
    else :
        return None

def check_Rows(board,player):
    for row in range(len(board)):
        count = 0
        for col in range(len(board[0])):
             if board[row][col] == player:
                count += 1
        if count == len(board[0]):
            return True
    return False             

def check_columns(board,player):
    for row in range(len(board[0])):
        count = 0
        for col in range(len(board)):
             if board[row][col] == player:
                count += 1
        if count == len(board[0]):
            return True
    return False

def check_TopBottomDiagonal(board,player):
    count = 0
    for row in range(len(board)):
        count = 0
        for col in range(len(board[0])):
            if row == col and board[row][col] == player:
                count += 1
    return count == len(board[0])
            
def check_BottomTopDiagonal(board,player):
    count = 0
    for row in range(len(board)):
        count = 0
        for col in range(len(board[0])):
            if (len(board)-row-1) == col and board[row][col] == player:
                count += 1
    return count == len(board[0])

def IsTie(board):
    countboard = (len(board) * len(board[0]))
    for row in range(len(board)):
        count = 0
        for col in range(len(board[0])):
            if board[row][col] is not EMPTY:
                countboard -= 1
    return countboard == 0




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or IsTie(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        arr = []
        for action in actions(board):
            arr.append([min_value(result(board,action)),action])
        return sorted(arr,key = lambda x:x[0], reserve=True)[0][1]
    elif player(board) == O:
         arr = []
         for action in actions(board):
             arr.append([max_value(result(board,action)),action])
         return sorted(arr,key = lambda x:x[0])[0][1]



def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v
     
def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v     