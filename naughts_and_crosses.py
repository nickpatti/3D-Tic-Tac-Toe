board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

turn_number = 0
win = False


def board_current(turn_number):
    print("Turn:", turn_number)

    if turn_number % 2 == 0:
        print("O's turn")
    else:
        print("X's turn")

    for row in board:
        print(row)
    print('\n')


def turn(turn_number):

    try:
        turn_pick = input("select your row in this format: row,column: ")
        turn_split = turn_pick.split(",")
        turn_row = int(turn_split[0])
        turn_column = int(turn_split[1])

        while board[turn_row][turn_column] > 0:
            turn_pick = input("Space has already been picked, pick again: ")
            turn_split = turn_pick.split(",")
            turn_row = int(turn_split[0])
            turn_column = int(turn_split[1])

        if turn_number % 2 == 0:
            board[turn_row][turn_column] = 1
        else:
            board[turn_row][turn_column] = 2
    except IndexError as e:
        print("Please select a number from 0-2", e)


def win_condition(game):

    column = []
    diag = []
    back_diag = []

    global win
    # horizontal win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] > 0:
            if turn_number % 2 == 0:
                print("O's win horizontally")
            else:
                print("X's win horizontally")
            win = True

    # vertical win

    for col in range(len(board)):
        column = []

        for row in board:
            column.append(row[col])

        if column.count(row[0]) == len(row) and column[0] > 0:
            if turn_number % 2 == 0:
                print("O's win vertically")
            else:
                print("X's win vertically")
            win = True
    # diagonal win
    diag = []
    back_diag = []

    for x in range(len(board)):
        diag.append(board[x][x])

        if diag.count(board[x][x]) == len(board) and row[x] > 0:
            if turn_number % 2 == 0:
                print("O's win diagonally")
            else:
                print("X's win diagonally")
            win = True

    for row, col in enumerate(reversed(range(len(board)))):
        back_diag.append(board[row][col])

        if back_diag.count(board[row][col]) == len(board) and back_diag[0] > 0:
            if turn_number % 2 == 0:
                print("O's win diagonally")
            else:
                print("X's win diagonally")
            win = True


for x in range(9):
    while win is False:
        board_current(turn_number)
        turn(turn_number)
        win_condition(board)
        turn_number += 1

for row in board:
    print(row)
