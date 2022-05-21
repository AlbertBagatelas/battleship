# The variable for the board
board = []

# To create 5 lists to act as rows
for i in range(0,5):
    board.append(["0"] *5)

# Function to put board as a stack to become a grid
def display_board(board):
    for i in board:
        print(i)

display_board(board)