from behave import *
from tictactoe import EMPTY_BOARD, play, play_best_move

@given(u'we have an empty tic-tac-toe board')
def step_impl(context):
    context.board = EMPTY_BOARD
    assert context.board == EMPTY_BOARD

@when(u'I play {p} on column {c} and row {r} on the board')
def step_impl(context, p, c, r):
    player=p
    column=int(c)-1
    row=int(r)-1
    ## play the game
    context.board, context.winner = play(context.board, player, column, row)
    context.position=3*row+column

@when(u'I ask the computer to do its best move for {p}')
def step_impl(context, p):
    player=p
    context.board, context.winner = play_best_move(context.board, player)

@then(u'the board has a {player} in column {c} and row {r} on the board')
def step_impl(context, player, c, r):
    c=int(c)-1
    r=int(r)-1
    #| 0 1 2 |#
    #| 3 4 5 |#
    #| 6 7 8 |#
    columns = [[0,3,6], [1,4,7], [2,5,8]]
    rows = [[0,1,2], [3,4,5], [6,7,8]]
    column=columns[c]
    row=rows[r]
    assert player in [context.board[c] for c in column] and player in [context.board[r] for r in row]

@then(u'{player} is the winner of the game')
def step_impl(context, player):
    assert context.winner==player
