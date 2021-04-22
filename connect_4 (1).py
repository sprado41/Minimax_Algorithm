# -*- coding: utf-8 -*-
"""
Created on Sat Mar 6 21:00:00 2021

@author: Sebastian Prado
"""

import math
import random
from copy import copy, deepcopy


ROWS = 6
COLS = 7
NUM_MATCHES = 10


def check_bounds(row, col):
    if ROWS > row >= 0 and COLS > col >= 0:
        return True
    else:
        return False


def score_board(board, player):
    total = 0
    symbol = 0
    enemy = 0
    score = 0

    if player == 1:
        symbol = 1
        enemy = 2
    if player == 2:
        symbol = 2
        enemy = 1
    for col in range(COLS):
        for row in range(ROWS - 1, 0, -1):
            game_location = [row, col]
            if game_location == 0:
                break
            score += evaluate_direction(board, game_location, symbol, enemy)  # total = value
        total += score
    return total


def evaluate_direction(board, game_piece, symbol, enemy):
    score = 0
    #  Check the right for player
    if check_bounds(game_piece[0], (game_piece[1] + 1)):
        if board[game_piece[0]][game_piece[1]] == symbol:
            if board[game_piece[0]][game_piece[1] + 1] == 0:
                score += 1
            if board[game_piece[0]][(game_piece[1] + 1)] == symbol:
                score += 2
                if check_bounds(game_piece[0], game_piece[1] + 2):
                    if board[game_piece[0]][game_piece[1] + 2] == symbol:
                        score += 5
                    elif board[game_piece[0]][game_piece[1] + 2] == enemy:
                        score -= 2
                    else:
                        score += 1
            if board[game_piece[0]][(game_piece[1] + 1)] == enemy:
                score += 0
        elif board[game_piece[0]][game_piece[1]] == enemy:
            if board[game_piece[0]][(game_piece[1] + 1)] == enemy:
                score -= 3
                if check_bounds(game_piece[0], game_piece[1] + 2):
                    if board[game_piece[0]][game_piece[1] + 2] == enemy:
                        score -= 1
                    elif board[game_piece[0]][game_piece[1] + 2] == symbol:
                        score += 3
            elif board[game_piece[0]][(game_piece[1] + 1)] == symbol:
                score += 0
    #  Check Up
    if check_bounds(game_piece[0] - 1, game_piece[1]):
        if board[game_piece[0]][game_piece[1]] == symbol:
            if board[game_piece[0] - 1][game_piece[1]] == 0:
                score += 1
            if board[game_piece[0] - 1][game_piece[1]] == symbol:
                score += 2
                if check_bounds(game_piece[0] - 2, game_piece[1]):
                    if board[game_piece[0] - 2][game_piece[1]] == symbol:
                        score += 2
                    elif board[game_piece[0] - 2][game_piece[1]] == enemy:
                        score -= 2
                    else:
                        score += 1
            if board[game_piece[0] - 1][game_piece[1]] == enemy:
                score += 0
        elif board[game_piece[0]][game_piece[1]] == enemy:
            if board[game_piece[0] - 1][(game_piece[1])] == enemy:
                score -= 3
                if check_bounds(game_piece[0] - 2, game_piece[1]):
                    if board[game_piece[0] - 2][game_piece[1]] == enemy:
                        score -= 1
                    elif board[game_piece[0] - 2][game_piece[1]] == symbol:
                        score += 3
            elif board[game_piece[0] - 1][(game_piece[1])] == symbol:
                score += 0
    # check upper right
    if check_bounds(game_piece[0], (game_piece[1] + 1)):
        if board[game_piece[0]][(game_piece[1] + 1)] != 0:
            if check_bounds(game_piece[0] - 1, (game_piece[1] + 1)):
                if board[game_piece[0]][(game_piece[1])] == symbol:
                    if board[game_piece[0] - 1][(game_piece[1] + 1)] == 0:
                        score += 1
                    if board[game_piece[0] - 1][(game_piece[1] + 1)] == symbol:
                        score += 2
                        if check_bounds(game_piece[0] - 2, (game_piece[1] + 2)):
                            if board[game_piece[0] - 2][(game_piece[1] + 2)] == symbol:
                                score += 2
                            elif board[game_piece[0] - 2][(game_piece[1] + 2)] == enemy:
                                score -= 2
                            else:
                                score += 1
                    if board[game_piece[0] - 1][(game_piece[1] + 1)] == enemy:
                        score += 0
                elif board[game_piece[0]][game_piece[1]] == enemy:
                    if board[game_piece[0] - 1][game_piece[1] + 1] == enemy:
                        score -= 3
                        if check_bounds(game_piece[0] - 2, game_piece[1] + 2):
                            if board[game_piece[0] - 2][game_piece[1] + 2] == enemy:
                                score -= 1
                            elif board[game_piece[0] - 2][game_piece[1] + 2] == symbol:
                                score += 3
                    elif board[game_piece[0] - 1][(game_piece[1] + 1)] == symbol:
                        score += 0
        else:
            score -= 4
    #  check left
    if check_bounds(game_piece[0], (game_piece[1] - 1)):
        if board[game_piece[0]][(game_piece[1])] == symbol:
            if board[game_piece[0]][(game_piece[1] - 1)] == 0:
                score += 1
            if board[game_piece[0]][(game_piece[1] - 1)] == symbol:
                score += 2
                if check_bounds(game_piece[0], game_piece[1] - 2):
                    if board[game_piece[0]][game_piece[1] - 2] == symbol:
                        score += 2
                    elif board[game_piece[0]][game_piece[1] - 2] == enemy:
                        score -= 2
                    else:
                        score += 1
            if board[game_piece[0]][(game_piece[1] - 1)] == enemy:
                score += 0
        elif board[game_piece[0]][game_piece[1]] == enemy:
            if board[game_piece[0]][(game_piece[1] - 1)] == enemy:
                score -= 3
                if check_bounds(game_piece[0], game_piece[1] - 2):
                    if board[game_piece[0]][game_piece[1] - 2] == enemy:
                        score -= 1
                    elif board[game_piece[0]][game_piece[1] - 2] == symbol:
                        score += 3
            elif board[game_piece[0]][(game_piece[1] - 1)] == symbol:
                score += 0

    # check upper left
    if check_bounds(game_piece[0], (game_piece[1] - 1)):
        if board[game_piece[0]][(game_piece[1] - 1)] != 0:  # Checks to see if there is a piece to the left
            if check_bounds(game_piece[0] - 1, (game_piece[1] - 1)):
                if board[game_piece[0]][(game_piece[1])] == symbol:
                    if board[game_piece[0] - 1][(game_piece[1] - 1)] == 0:
                        score += 1
                    if board[game_piece[0] - 1][(game_piece[1] - 1)] == symbol:
                        score += 2
                        if check_bounds(game_piece[0] - 2, (game_piece[1] - 2)):
                            if board[game_piece[0] - 2][(game_piece[1] - 2)] == symbol:
                                score += 2
                            elif board[game_piece[0] - 2][(game_piece[1] - 2)] == enemy:
                                score -= 2
                            else:
                                score += 1
                    if board[game_piece[0] - 1][(game_piece[1] - 1)] == enemy:
                        score -= 4
                elif board[game_piece[0]][game_piece[1]] == enemy:
                    if board[game_piece[0] - 1][game_piece[1] - 1] == enemy:
                        score -= 3
                        if check_bounds(game_piece[0] - 2, game_piece[1] - 2):
                            if board[game_piece[0] - 2][game_piece[1] - 2] == enemy:
                                score -= 1
                            elif board[game_piece[0] - 2][game_piece[1] - 2] == symbol:
                                score += 3
                    elif board[game_piece[0] - 1][(game_piece[1] - 1)] == symbol:
                        score += 0
        else:  # if not then move is not possible this turn
            score -= 4
        # check lower left
        if check_bounds(game_piece[0], (game_piece[1] + 1)):
            if board[game_piece[0]][(game_piece[1] + 1)] != 0:  # Checks to see if there is a piece to the left
                if check_bounds(game_piece[0] + 1, (game_piece[1] - 1)):
                    if board[game_piece[0]][(game_piece[1])] == symbol:
                        if board[game_piece[0] + 1][(game_piece[1] - 1)] == 0:
                            score += 1
                        if board[game_piece[0] + 1][(game_piece[1] - 1)] == symbol:
                            score += 2
                            if check_bounds(game_piece[0] + 2, (game_piece[1] - 2)):
                                if board[game_piece[0] + 2][(game_piece[1] - 2)] == symbol:
                                    score += 2
                                elif board[game_piece[0] + 2][(game_piece[1] - 2)] == enemy:
                                    score -= 2
                                else:
                                    score += 1
                        if board[game_piece[0] + 1][(game_piece[1] - 1)] == enemy:
                            score -= 4
                    elif board[game_piece[0]][game_piece[1]] == enemy:
                        if board[game_piece[0] + 1][game_piece[1] - 1] == enemy:
                            score -= 3
                            if check_bounds(game_piece[0] + 2, game_piece[1] - 2):
                                if board[game_piece[0] + 2][game_piece[1] - 2] == enemy:
                                    score -= 1
                                elif board[game_piece[0] + 2][game_piece[1] - 2] == symbol:
                                    score += 3
                        elif board[game_piece[0] + 1][(game_piece[1] - 1)] == symbol:
                            score += 0
            else:  # if not then move is not possible this turn
                score -= 4
            # check lower right
            if check_bounds(game_piece[0] + 2, (game_piece[1] + 1)):
                if board[game_piece[0] + 2][(game_piece[1] + 1)] != 0:
                    if check_bounds(game_piece[0] + 1, (game_piece[1] + 1)):
                        if board[game_piece[0]][game_piece[1]] == symbol:
                            if board[game_piece[0] + 1][(game_piece[1] + 1)] == 0:
                                score += 1
                            if board[game_piece[0] + 1][(game_piece[1] + 1)] == symbol:
                                score += 2
                                if check_bounds(game_piece[0] + 2, (game_piece[1] + 2)):
                                    if board[game_piece[0] + 2][(game_piece[1] + 2)] == symbol:
                                        score += 2
                                    elif board[game_piece[0] + 2][(game_piece[1] + 2)] == enemy:
                                        score -= 2
                                    else:
                                        score += 1
                            if board[game_piece[0] + 1][(game_piece[1] + 1)] == enemy:
                                score -= 2
                        elif board[game_piece[0]][game_piece[1]] == enemy:
                            if board[game_piece[0] + 1][game_piece[1] + 1] == enemy:
                                score -= 3
                                if check_bounds(game_piece[0] + 2, game_piece[1] + 2):
                                    if board[game_piece[0] + 2][game_piece[1] + 2] == enemy:
                                        score -= 1
                                    elif board[game_piece[0] + 2][game_piece[1] + 2] == symbol:
                                        score += 3
                            elif board[game_piece[0] + 1][(game_piece[1] - 1)] == symbol:
                                score += 0
                else:
                    score -= 4
    return score


def is_valid_location(board, col):
    if board[0][col] == 0:
        return True
    else:
        return False


def possible_locations(board):
    locations = []
    for col in range(COLS):
        if is_valid_location(board, col):
            locations.append(col)
    return locations


def next_row(board, col):
    for i in range(ROWS - 1, -1, -1):
        if board[i][col] == 0:
            return i


def drop_piece(board, row, col, player):
    board[row][col] = player


def minimax(board, depth, alpha, beta, player_maximizing, player):
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    possible_moves = possible_locations(board)
    column = 0
    if depth == 0:
        return [None, score_board(board, player)]
    if player_maximizing:
        v = -math.inf
        for col in possible_moves:
            row = next_row(board, col)
            connect_board = deepcopy(board)
            drop_piece(connect_board, row, col, player)
            score = minimax(connect_board, depth - 1, alpha, beta, False, player)
            if score[1] > v:
                v = score[1]
                column = col
            alpha = max(v, alpha)
            if alpha >= beta:
                break
        return [column, v]
    else:  # minimizing player
        v = math.inf
        for col in possible_moves:
            row = next_row(board, col)
            connect_board = deepcopy(board)
            drop_piece(connect_board, row, col, opponent)
            score = minimax(connect_board, depth - 1, alpha, beta, True, player)
            if score[1] < v:
                v = score[1]
                column = col
            beta = min(v, beta)
            if alpha >= beta:
                break
        return [column, v]


# This is what is called at Main
def mini_max_function(board, player_turn):
    depth = 4
    alpha = -math.inf
    beta = math.inf
    next_move = minimax(board, depth, alpha, beta, True, player_turn)
    col = next_move[0]
    row = next_row(board, col)
    drop_piece(board, row, col, player_turn)
    return col
