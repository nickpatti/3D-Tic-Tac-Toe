board = [[1, 0, 1],
         [0, 1, 0],
         [1, 0, 1]]

# horizontal win
for row in board:
    if row.count(row[0]) == len(row) and row[0] > 0:
        print("horizontal winner")

# vertical win

for col in range(len(board)):
    column = []

    for row in board:
        column.append(row[col])

    if column.count(row[0]) == len(row) and column[0] > 0:
        print("vertical winner")
# diagonal win
diag = []
back_diag = []

for x in range(len(board)):
    diag.append(board[x][x])

    if diag.count(board[x][x]) == len(board) and row[x] > 0:
        print("r diag winner")


for row, col in enumerate(reversed(range(len(board)))):
    back_diag.append(board[row][col])

    if back_diag.count(board[row][col]) == len(board) and back_diag[0] > 0:
        print("l diag winner")

# for row in board:
#     back_diag.append(row[len(board) - y])
#     y += 1

#     if back_diag.count(row[len(board) - y]) == len(back_diag) and back_diag[len(board) - y] > 0:
#         print("l diag winner") this one didn't work
