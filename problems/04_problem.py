"""
PART 4: Bingo

Bingo rules - 5 x 5 grid. Win if all 5 in col or row selected (no diagonals).

First line if input is order numbers are drawn.
Remaining lines are bingo grids.

Ex:
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19
"""
import copy
import numpy as np

# Four tasks (delete later):
# 1. parse input
# 2. search boards for called nums
# 3. look for complete rows and cols - replace called vals with -1 (or something) to note as called, look for sum of -5
# 4. calculate score

# Parse input.
raw_input = open('04_input.txt', 'r').readlines()

draw_order = [int(x) for x in raw_input[0].strip().split(',')]

boards = []
for i in range(len(raw_input)-2)[2::6]:
    one_board = np.array([l.strip().split() for l in raw_input[i:i+5]]).astype(int)
    boards.append(one_board)


def is_winner(board, call_mark=-1):
    """
    Takes in board and determines if row or col is complete.
    :param board: np.array 5 x 5
    :param call_mark: int used to mark a cell as having been called (replaces original value)
    :return: True if winner
    """
    desired_sum = call_mark * len(board)
    row_sum = board.sum(axis=1)
    col_sum = board.sum(axis=0)
    if (row_sum == desired_sum).any() or (col_sum == desired_sum).any():
        winner = True
    else:
        winner = False
    return winner

# Part 1: Find winning grid and sum all UNMARKED numbers and multiply but the final (winning) number called.
call_marker = -1
board_is_winner = [False] * len(boards)
game_boards = copy.deepcopy(boards) # Basically  making a copy. copy() never works as intended....
for called_num in draw_order:
    for i, b in enumerate(game_boards):
        b[b == called_num] = call_marker
        win = is_winner(b, call_mark=call_marker)
        if win:
            board_is_winner[i] = win
    if any(board_is_winner):
        break

winning_board = game_boards[board_is_winner.index(True)] # Note: will return only first winner. Assume that's ok for now.
winning_board[winning_board == call_marker] = 0

print(f"Winning score: {winning_board.sum() * called_num}")


# Part 2: Now find the last board that would win and calculate score the same way.
# Feeling too lazy to clean the above so just copy and update as needed.
call_marker = -1
board_is_winner = [False] * len(boards)
game_boards2 = copy.deepcopy(boards)
for called_num in draw_order:
    remaining_to_win = [i for i, board_has_won in enumerate(board_is_winner) if not board_has_won]
    print(f"Num remaining to win: {len(remaining_to_win)}")
    if len(remaining_to_win) == 0:
        break
    for i in remaining_to_win:
        b = game_boards2[i]
        b[b == called_num] = call_marker
        win = is_winner(b, call_mark=call_marker)
        if win:
            board_is_winner[i] = win
            if sum(board_is_winner) == len(board_is_winner):
                last_board = b
                last_called = called_num


last_board[last_board == call_marker] = 0

print(f"Winning score: {last_board.sum() * last_called}")
