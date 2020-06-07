"""
Tic Tac Toe Player
"""

import math
import copy

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

    for x in board:
        for y in x:
            if y==X: countX += 1
            if y==O: countO += 1

    if countX==countO: return X
    if countX>countO: return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for x in range(3):
        for y in range(3):
            if board[x][y]==EMPTY:
                moves.add((x,y))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)

    if newBoard[action[0]][action[1]] == EMPTY:
        newBoard[action[0]][action[1]] = player(board)
        return newBoard

    else: raise Exception("Invalid Action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[2][2]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[2][0]
    for x in range(3):
        if board[x][0] == board[x][1] and board[x][1] == board[x][2]:
            return board[x][2]
        if board[0][x] == board[1][x] and board[1][x] == board[2][x]:
            return board[2][x]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    elif actions(board):
        return False
    else: return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    else: return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board)==X:
        maxU = -1
        todo = (-1,-1)
        for pAction in actions(board):
            score = findMin(result(board, pAction))
            if score > maxU:
                maxU = score
                todo = pAction
        return todo
    if player(board)==O:
        minU = 1
        todo = (-1,-1)
        for pAction in actions(board):
            score = findMax(result(board, pAction))
            if score < minU:
                minU = score
                todo = pAction
        return todo


def findMax(board):
    """
    Returns the maximum score for all possible actions of a given board.
    """
    if terminal(board):
        return utility(board)
    maxU = -1
    for pActions in actions(board):
        maxU = max(maxU, findMin(result(board, pActions)))
    return maxU


def findMin(board):
    """
    Returns the minimum score for all possible actions of a given board.
    """
    if terminal(board):
        return utility(board)
    minU = 1
    for pActions in actions(board):
        minU = min(minU, findMax(result(board, pActions)))
    return minU
