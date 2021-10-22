'''
This is the whiteboard for checking feautre functions
'''

from tictactoe import play_console_game as ttt
from tictactoe import EMPTY_BOARD, play

#######################
## 1,1 ## 2,1 ## 3,1 ##
#######################
## 1,2 ## 2,2 ## 3,2 ##
#######################
## 1,3 ## 2,3 ## 3,3 ##
#######################

from tictactoe import EMPTY_BOARD, play, play_best_move

board = EMPTY_BOARD # clear the 3 x 3 tictactoe board
winner = None # set the winner to None

#oard, winner = play(board, 'O', 0, 0)
#board, winner = play(board, 'O', 1, 0)
#board, winner = play(board, 'X', 2, 0)

if True:
    board, winner = play(board, 'O', 0, 0)
    board, winner = play_best_move(board, 'X')
    board, winner = play(board, 'O', 2, 2)
    board, winner = play_best_move(board, 'X')
    board, winner = play(board, 'O', 1, 2)
    board, winner = play_best_move(board, 'X')
    board, winner = play(board, 'O', 2, 0)
    board, winner = play_best_move(board, 'X')
    board, winner = play(board, 'O', 0, 1)

    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

if False:
    player='O'
    c='1'
    r='1'
        
    c=int(c)-1
    r=int(r)-1
    #| 0 1 2 |#
    #| 3 4 5 |#
    #| 6 7 8 |#
    columns = [[0,3,6], [1,4,7], [2,5,8]]
    rows = [[0,1,2], [3,4,5], [6,7,8]]
    column=columns[c]
    row=rows[r]

    #print(type((column[:]))

    if player in [board[c] for c in column] and player in [board[r] for r in row]:
        print(True)