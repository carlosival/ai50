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
    countX = 0
    countO = 0

    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1
    
    return X if countX == countO else O 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row, idxr in enumerate(board):
        for cell, idxc in enumerate(idxr):
            if idxc == EMPTY:
                actions.add((row, cell))
    return actions           


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise RuntimeError("Invalid Action")

    newboard = [[cell for cell in row] for row in board]

    turn = player(newboard)

    newboard[action[0]][action[1]] = turn
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wplayer = check_cols(board)
    if wplayer != None:
        return wplayer
    wplayer = check_rows(board)
    if wplayer != None:
        return wplayer
    return check_digs(board)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    won = winner(board)
    
    if won != None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
     
    won = winner(board)

    if won == O: 
        return -1
    if won == X: 
        return 1

    return 0


def minimaxhelper(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return (None, utility(board), None)
    turn = player(board)
    if turn == X:
        best = -2
        optimal = None
        for action in actions(board):  
            next_board = result(board, action)
            (_, value, _) = minimaxhelper(next_board)
            if best < value:
                best = value
                optimal = action
        return (optimal, best, turn)
    else:
        best = 2
        optimal = None
        for action in actions(board):
            next_board = result(board, action)
            (_, value, _) = minimaxhelper(next_board)
            if best > value:
                best = value
                optimal = action 
        return (optimal, best, turn)
    

def minimax(board):
    (action, score, turn) = minimaxhelper(board)
    return action


def check_row(board, row):
    col = 0
    start = board[row][col]
    while col < len(board) and start != EMPTY and start == board[row][col]:
        col += 1
    return start if col == len(board) else None


def check_col(board, col):
    row = 0
    start = board[row][col]
    while row < len(board) and start != EMPTY and start == board[row][col]:
        row += 1
    return start if row == len(board) else None


def check_rows(board):
    result = None
    for i in range(3):
        result = check_row(board, i)
        if result != None: 
            return result
    return result


def check_cols(board):
    result = None
    for i in range(3):
        result = check_col(board, i)
        if result != None: 
            return result
    return result


def check_digs(board):
    middle = board[1][1]

    if middle == EMPTY:
        return None
    
    if middle == board[0][0] and board[2][2] == middle:
        return middle
    
    if middle == board[2][0] and board[0][2] == middle:
        return middle
    
    return None



