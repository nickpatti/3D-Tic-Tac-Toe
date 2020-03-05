board = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
         [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

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
        turn_pick = input("select your row in this format: y,z,x: ")
        turn_split = turn_pick.split(",")
        turn_y = int(turn_split[0])
        turn_z = int(turn_split[1])
        turn_x = int(turn_split[2])

        while board[turn_y][turn_z][turn_x] > 0:
            turn_pick = input("Space has already been picked, pick again: ")
            turn_split = turn_pick.split(",")
            turn_y = int(turn_split[0])
            turn_z = int(turn_split[1])
            turn_x = int(turn_split[2])

        if turn_number % 2 == 0:
            board[turn_y][turn_z][turn_x] = 1
        else:
            board[turn_y][turn_z][turn_x] = 2
    except IndexError as e:
        print("Please select a number from 0-2", e)


def win_condition(game):

    column = []
    diag = []
    back_diag = []

    global win
    # horizontal win
    for row in board:
        for x in row:
            if x.count(x[0]) == len(x) and x[0] > 0:
                print("horizontal winner")

    # VERTICAL WIN

    # get a number incremented by 1 ending on 2 and repeat this three times 0,1,2 0,1,2 0,1,2
    # for now, z dimension will always have 3 integers, set z as a list and for loop over it, when x = z we know only the column is changing
    for x in range(len(board)):
        for height in range(len(board)):

            if x == z[x]:
                for col in range(len(board)):
                    column = []

                for y in range(len(board)):
                    # below - not really x, just x when it = z
                    column.append(board[y][x][height])

                    if column.count(column[0]) == len(row) and column[0] > 0:
                        print("vertical winner")
                        win = True

    # Z WIN - same as vertical win, but x and y change, z stays the same

    for x in range(len(board)):
        for y in range(len(board)):

            if x == y:
                for col in range(len(board)):
                    z_vert = []

                for height in range(len(board)):
                    z_vert.append(board[y][height][x])

                    if z_vert.count(z_vert[0]) == len(row) and z_vert[0] > 0:
                        print("z_vert winner")
                        win = True

    # FLAT DIAGONAL WIN - new win conditions: [0][0][0], 111, 222      ,     010 111, 222      ,    020 121 222

    for z in range(len(board)):
        diag = []
        for x in range(len(board)):
            # x and y remain the same, just using x in place of y here
            diag.append(board[x][z][x])

        if diag.count(board[x][z][x]) == len(board) and diag[0] > 0:
            print("flar r diag winner", diag)
            win = True

    # new win coniditions reverse diagonal: 002, 001, 000     012, 011, 010,     022, 021, 020
    # need to add the z dimension which will be the same every iteration - has to be the first for loop... surprisingly easy

    for z in range(len(board)):
        back_diag = []
        for x, y in enumerate(reversed(range(len(board)))):
            back_diag.append(board[y][z][x])

            if back_diag.count(board[y][z][x]) == len(board) and back_diag[0] > 0:
                print("flat l diag winner", back_diag)
                win = True

    limit = (len(board) - 1)
    for y in range(len(board)):
        for x in range(len(board)):
            if x == 0 and y == 0:
                z_diag = []
                z_diag2 = []
                corner_diag = []
                for z in range(len(board)):
                    # these two are face digaonals

                    z_diag.append(board[0][z][z])
                    z_diag2.append(board[z][z][0])
                    # this is a corner diagonal:
                    corner_diag.append(board[z][z][z])

                    if z_diag.count(board[0][z][z]) == len(board) and z_diag[0] > 0:
                        print("3d diag winner", z_diag)
                        win = True
                    if z_diag2.count(board[z][z][0]) == len(board) and z_diag2[0] > 0:
                        print("3d diag winner", z_diag2)
                        win = True
                    if corner_diag.count(board[z][z][z]) == len(board) and corner_diag[0] > 0:
                        print("corner diag winner", corner_diag)
                        win = True

            if x == 0 and y == limit:
                z = 0
                z_diag = []
                z_diag2 = []
                corner_diag = []

                for c in reversed(range(len(board))):
                    # face diagonals
                    z_diag.append(board[c][z][0])
                    z_diag2.append(board[limit][z][z])
                    # corner diagonal
                    corner_diag.append(board[c][z][z])

                    if z_diag.count(board[c][z][0]) == len(board) and z_diag[0] > 0:
                        print("3d diag winner", z_diag)
                        win = True
                    if z_diag2.count(board[limit][z][z]) == len(board) and z_diag2[0] > 0:
                        print("3d diag winner", z_diag2)
                        win = True
                    if corner_diag.count(board[c][z][z]) == len(board) and corner_diag[0] > 0:
                        print("corner diag winner", corner_diag)
                        win = True

                    # had to put z after the check loops so list index is in range
                    z += 1

            if x == limit and y == 0:
                z = 0
                z_diag = []
                z_diag2 = []
                corner_diag = []

                for c in reversed(range(len(board))):
                    z_diag.append(board[0][z][c])
                    z_diag2.append(board[z][z][limit])
                    # corner diagonal
                    corner_diag.append(board[z][z][c])

                    if z_diag.count(board[0][z][c]) == len(board) and z_diag[0] > 0:
                        print("3d diag winner", z_diag)
                        win = True
                    if z_diag2.count(board[z][z][limit]) == len(board) and z_diag2[0] > 0:
                        print("3d diag winner", z_diag2)
                        win = True
                    if corner_diag.count(board[z][z][c]) == len(board) and corner_diag[0] > 0:
                        print("corner diag winner", corner_diag)
                        win = True
                    z += 1

            if x == limit and y == limit:
                z = 0
                z_diag = []
                z_diag2 = []
                corner_diag = []

                for c in reversed(range(len(board))):
                    z_diag.append(board[limit][z][c])
                    z_diag2.append(board[c][z][limit])
                    # corner diagonal
                    corner_diag.append(board[c][z][c])

                    if z_diag.count(board[limit][z][c]) == len(board) and z_diag[0] > 0:
                        print("3d diag winner", z_diag)
                        win = True
                    if z_diag2.count(board[c][z][limit]) == len(board) and z_diag2[0] > 0:
                        print("3d diag winner", z_diag2)
                        win = True
                    if corner_diag.count(board[c][z][c]) == len(board) and corner_diag[0] > 0:
                        print("corner diag winner", corner_diag)
                        win = True
                    z += 1

            if y != limit and y != 0:
                z = 0
                middle_diag = []
                middle_diag2 = []
                for z in range(len(board)):
                    middle_diag.append(board[y][z][z])

                    if middle_diag.count(board[y][z][z]) == len(board) and middle_diag[0] > 0:
                        print("middle diag winner", middle_diag)
                        win = True

                    z += 1

                z = 0
                for c in reversed(range(len(board))):
                    middle_diag2.append(board[y][z][c])

                    if middle_diag2.count(board[y][z][c]) == len(board) and middle_diag2[0] > 0:
                        print("middle diag winner", middle_diag2)
                        win = True
                    z += 1

            if x != limit and x != 0 and y == 0:
                middle_diag = []
                middle_diag2 = []
                z = 0
                for z in range(len(board)):
                    middle_diag.append(board[z][z][x])

                    if middle_diag.count(board[z][z][x]) == len(board) and middle_diag[0] > 0:
                        print("middle diag winner", middle_diag)
                        win = True
                    z += 1

                z = 0
                for c in reversed(range(len(board))):
                    middle_diag2.append(board[c][z][x])

                    if middle_diag2.count(board[c][z][x]) == len(board) and middle_diag2[0] > 0:
                        print("middle diag winner", middle_diag2)
                        win = True
                    z += 1

#36 maximum moves in 3d
while win is False:
         board_current(turn_number)
         turn(turn_number)
         win_condition(board)
         turn_number += 1
         
         if turn_number = 37 and win == False:
                  print("Draw"!)
                  break;
        
for row in board:
    print(row)
