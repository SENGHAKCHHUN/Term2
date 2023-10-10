# Define your 2D array
array2D = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
# Function to display the array
def print_board(board):
    output = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            output += board[i][j]
            if j != len(board[i]) - 1:
                output += " | "
        if i != len(board) - 1:
            output += "\n" + "---------"+'\n'
    return output

# return true if row are matching together with 3 otherwise false
# xox
def check_row(array2D, symbol):
    for i in range(len(array2D)):
        row_matches = True
        for j in range(len(array2D)):
            if array2D[i][j] != symbol:
                row_matches = False
        if row_matches:
            return True  
    return False
# return true if column are matching together with 3 other false
# x
# x
# x
def check_column(array2D, symbol):
    for row in range(len(array2D)):
        col_matches = True
        for col in range(len(array2D)):
            if array2D[col][row] != symbol:
                col_matches = False
        if col_matches:
            return True
    return False

# return true if diagonal are mathcing together with 3 other false
def check_diagonal(array2D, symbol):
    # Check the main diagonal (top-left to bottom-right)
    diagonal1_matches = True
    for i in range(len(array2D)):
        if array2D[i][i] != symbol:
            diagonal1_matches = False
    
    # Check the other diagonal (top-right to bottom-left)
    diagonal2_matches = True
    for i in range(len(array2D)):
        if array2D[i][2 - i] != symbol:
            diagonal2_matches = False
    
    return diagonal1_matches or diagonal2_matches

# return true if function check_row or check_column or check_diagonal are true else false
def check_tic_tac_toe_winner(array2D, symbol):
    if (check_row(array2D, symbol) or
        check_column(array2D, symbol) or
        check_diagonal(array2D, symbol)):
        return True
    return False

print("Welcome to Tic-Tac-Toe!")
print(print_board(array2D))

current_player = 'X'
not_win = 'Not Win'

while not_win == 'Not Win':
    rowColumn = eval(input("Player " + current_player + ", enter the row and column (e.g., (0, 0)): "))
    row = rowColumn[0]
    column = rowColumn[1]

    if array2D[row][column] == ' ':

        array2D[row][column] = current_player
        print(print_board(array2D))
        if check_tic_tac_toe_winner(array2D, current_player):
                not_win = "Player " + current_player + " wins!"
        if current_player == 'X':
            current_player = '0'
        else:
            current_player = 'X'
    else:
        print("Cell is already played. Choose another cell.")

print(not_win)
